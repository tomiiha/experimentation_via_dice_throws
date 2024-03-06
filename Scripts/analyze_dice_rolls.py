def analyze_dice_rolls(sample_size, dice_throws, rigging, significance_level=0.05, desired_power=0.8,show_results=False):

    # Play the games
    fair_dice, rigged_dice = play_games(sample_size, dice_throws, rigging)

    # Calculate the means
    mean_fair = np.mean(fair_dice)
    mean_rigged = np.mean(rigged_dice)

    # Calculate the pooled standard deviation
    std_dev = np.sqrt((np.std(fair_dice, ddof=1) ** 2 + np.std(rigged_dice, ddof=1) ** 2) / 2)

    # Conduct Levene's test for equality of variances
    levene_stat, levene_p = stats.levene(fair_dice, rigged_dice)

    # Calculate Cohen's d
    cohens_d = (mean_fair - mean_rigged) / std_dev

    # Calculate individual standard deviations
    std_dev_fair = np.std(fair_dice, ddof=1)
    std_dev_rigged = np.std(rigged_dice, ddof=1)

    # Calculate Cohen's d for independent standard deviations
    cohens_d_independent = (mean_fair - mean_rigged) / max(std_dev_fair, std_dev_rigged)

    # Perform power analysis
    power_analysis = smp.TTestIndPower()
    power = power_analysis.solve_power(effect_size=cohens_d, nobs1=sample_size, 
                                   alpha=significance_level, ratio=1, 
                                   alternative='two-sided')

    # Calculate sample sizes
    sample_size_pooled = power_analysis.solve_power(effect_size=cohens_d, alpha=significance_level, 
                                                    power=desired_power, ratio=1, 
                                                    alternative='two-sided')
    sample_size_independent = power_analysis.solve_power(effect_size=cohens_d_independent, alpha=significance_level, 
                                                         power=desired_power, ratio=1, 
                                                         alternative='two-sided')
    sample_size_pooled = int(sample_size_pooled)
    sample_size_independent = int(sample_size_independent)

    # Determine which test to use
    test_type = 2 if levene_p < significance_level else 1  # 2 for Welch’s t-test, 1 for standard t-test

    if show_results:
        print('---------------------------------')
        print(f"Mean Fair Throws: {round(mean_fair,1)}")
        print(f"Mean Rigged Throws: {round(mean_rigged,1)}")
        print(f"Pooled Standard Deviation: {round(std_dev,3)}")
        print('---------------------------------')
        print(f"Levene's Test Statistic: {levene_stat}")
        print(f"Levene's Test P-Value: {levene_p}")
        print('---------------------------------')
        print(f"Cohen's d: {round(cohens_d,3)}")
        print(f"Power (%): {round(power*100,1)}")
        print('---------------------------------')
        print(f"Sample Size (Pooled): {round(sample_size_pooled,0)}")
        print(f"Sample Size (Independent): {round(sample_size_independent,0)}")
        print('---------------------------------')

    # Return relevant statistics and test type
    return {
        "sample_size_pooled": sample_size_pooled,
        "sample_size_independent": sample_size_independent,
        "test_type": test_type
    }
