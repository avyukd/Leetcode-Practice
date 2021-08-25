class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> intersection;
        intersection.reserve((max(nums1.size(), nums2.size())));
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int nums1_idx = 0;
        int nums2_idx = 0;
        while(nums1_idx != nums1.size() && nums2_idx != nums2.size()){
            if(nums1[nums1_idx] < nums2[nums2_idx]){
                nums1_idx++;
            }else if(nums1[nums1_idx] > nums2[nums2_idx]){
                nums2_idx++;
            }else{
                intersection.push_back(nums1[nums1_idx]);
                nums1_idx++;
                nums2_idx++;
            }
        }
        return intersection;
        
    }
};