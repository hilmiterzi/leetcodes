import timeit


def median_merge(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2.0
    else:
        return merged[mid]


def median_binary_search(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return float(max_of_left)

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0
def median_binary_better_explained(nums1, nums2):
    # First, ensure nums1 is the smaller of the two arrays to optimize the search.
    # If nums1 is larger, we swap nums1 with nums2.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)

    # Binary search initialization: set search boundaries in the smaller array, nums1.
    beginning_index_nums1, ending_index_nums1 = 0, m

    # The variable total_length_half represents the half point of the combined arrays.
    # Adding 1 and using integer division ensures correct handling for both odd and even lengths.
    total_length_half = (m + n + 1) // 2

    # Start the binary search loop, which will continue until the correct median position is found.
    while beginning_index_nums1 <= ending_index_nums1:
        # Calculate the partition index for nums1.
        # Hier pakken we de helft van index 1 om vanaf daar te beginnen, en dat noemen we partittion of number 1
        partition_nums1 = (beginning_index_nums1 + ending_index_nums1) // 2
        # Determine the corresponding partition index in nums2 based on partition_nums1.
        partition_nums2 = total_length_half - partition_nums1

        # Check if the current partition in nums1 needs adjustment:
        # Condition 1: The element just right of partition in nums1 is less than the element just left of partition in nums2.
        if partition_nums1 < m and nums2[partition_nums2 - 1] > nums1[partition_nums1]:
            # Move the beginning_index_nums1 up to narrow the search range to the right.
            beginning_index_nums1 = partition_nums1 + 1
        # Condition 2: The element just left of partition in nums1 is greater than the element just right of partition in nums2.
        elif partition_nums1 > 0 and nums1[partition_nums1 - 1] > nums2[partition_nums2]:
            # Move the ending_index_nums1 down to narrow the search range to the left.
            ending_index_nums1 = partition_nums1 - 1
        else:
            # If the current partitions are correctly dividing the arrays according to the median calculation rules:
            # - The largest elements on the left are less than the smallest elements on the right.
            # This condition implies that we have found the correct partitions, and we proceed to calculate the median.
            # The function will return the median and exit, thus ending the loop and the function execution.

            max_of_left = float('-inf')
            if partition_nums1 > 0:
                max_of_left = max(max_of_left, nums1[partition_nums1 - 1])
            if partition_nums2 > 0:
                max_of_left = max(max_of_left, nums2[partition_nums2 - 1])

            # If the combined length of the arrays is odd, return max_of_left as the median.
            if (m + n) % 2 == 1:
                return max_of_left

            # Determine the smallest value on the right side of the partition:
            min_of_right = float('inf')
            if partition_nums1 < m:
                min_of_right = min(min_of_right, nums1[partition_nums1])
            if partition_nums2 < n:
                min_of_right = min(min_of_right, nums2[partition_nums2])

            # If the combined length of the arrays is even, return the average of max_of_left and min_of_right as the median.
            return (max_of_left + min_of_right) / 2.0

    # If valid partitions were not found (unlikely with valid input), return an error code.
    return -1



# Setup code for timeit
setup_code = """
from __main__ import median_merge, median_binary_search, median_binary_better_explained
import random
nums1 = sorted(random.sample(range(1000000), 500000))
nums2 = sorted(random.sample(range(1000000), 500000))
"""

# Test the merge approach
merge_time = timeit.timeit("median_merge(nums1, nums2)", setup=setup_code, number=10)
print("Average merge method time:", merge_time / 10)

# Test the binary search approach
binary_search_time = timeit.timeit("median_binary_better_explained(nums1, nums2)", setup=setup_code, number=10)
print("Average binary search method time:", binary_search_time / 10)

median_binary_better = timeit.timeit("median_binary_better_explained(nums1, nums2)", setup=setup_code, number=10)
print("Average better explained binary search method time:", binary_search_time / 10)
