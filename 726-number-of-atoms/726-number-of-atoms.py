class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        stack = deque([])
        
        i = 0
        while i < len(formula):
            ch = formula[i]
                        
            if ch.isupper():
                element = ch
                while i + 1 < len(formula) and formula[i + 1].islower():
                    element += formula[i + 1]
                    i += 1
                
                stack.append([element, 1])
                
            elif ch in ('(', ')'):
                stack.append([ch, 1])
                
            else:
                # ch is digit
                val = ch
                while i + 1 < len(formula) and formula[i + 1].isdigit():
                    val += formula[i + 1]
                    i += 1
                
                val = int(val)
                
                top, cnt = stack[-1]
                
                if top == ')':
                    stack.pop()
                    poppedEls = []
                    while stack[-1][0] != '(':
                        poppedEls.append(stack.pop())
                    stack.pop()
                    for el in poppedEls:
                        el[1] *= val
                        stack.append(el)
                else:
                    # element name
                    stack[-1][1] *= val
                
            i += 1
                
        elMap = defaultdict(int)
        for el, cnt in stack:
            if el not in ('(', ')'):
                elMap[el] += cnt
        
        pairs = []
        for k in elMap:
            pairs.append((k, elMap[k]))
        
        pairs.sort()
        
        return "".join([pair[0] + (str(pair[1]) if pair[1] > 1 else "") for pair in pairs])