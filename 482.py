class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        license_number = S.replace('-', '')
        group = 0
        result = ''
        for c in license_number[::-1]:
            if group < K:
                group += 1
                result = c.upper() + result
            else:
                result = c.upper() + '-' + result
                group = 1
        return result