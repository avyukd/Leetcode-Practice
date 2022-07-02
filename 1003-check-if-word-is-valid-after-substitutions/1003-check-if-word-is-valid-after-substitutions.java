class Solution {
        public boolean isValid(String S) {
while (S.contains("abc")) {
S = S.replaceAll("abc", "");
}
return S.length() == 0;
}
}