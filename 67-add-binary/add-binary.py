class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1 
        j = len(b) - 1

        carry = 0

        while i >= 0 or j >=0 or carry:
            int_a_bit = int(a[i]) if i >=0 else 0
            int_b_bit = int(b[j]) if j >=0 else 0
            sum = int_a_bit + int_b_bit + carry 
            carry = (sum // 2)
            res.append(str(sum % 2))

            i -=1
            j -=1
        return "".join(reversed(res))