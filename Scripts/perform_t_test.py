def perform_t_test(fair_dice_results, rigged_dice_results, test_type):
    # Choose the appropriate t-test based on the test_type
    if test_type == 1:  # Standard t-test
        t_statistic, p_value = stats.ttest_ind(fair_dice_results, rigged_dice_results, equal_var=True)
        test_name = "Standard t-test"
    elif test_type == 2:  # Welch’s t-test
        t_statistic, p_value = stats.ttest_ind(fair_dice_results, rigged_dice_results, equal_var=False)
        test_name = "Welch’s t-test"
    else:
        raise ValueError("Invalid test type. Choose 1 for Standard t-test or 2 for Welch’s t-test.")

    # Output the t-test results
    print(f"{test_name} Results:")
    print(f"T Statistic: {t_statistic}")
    print(f"P-Value: {p_value}")
