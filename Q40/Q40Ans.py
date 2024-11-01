def isitPrime(k):
    # 如果 k 等於 2 或 3，則是質數
    if k==2 or k==3: return True
    # 如果 k 是偶數或小於 2，則不是質數
    if k%2==0 or k<2: return False
    # 從 3 開始，以 2 為步進，檢查是否有因數
    for i in range(3, int(k**0.5)+1, 2):
        if k%i == 0:
            return False
    # 如果沒有找到因數，則是質數
    return True

def check(gen):
    if len(gen) == 0: # 空的基因
        return False
    if isitPrime(len(gen)): # 長度是質數
        return True
    return False

def matches_pattern(seq):
    # 序列長度必須為 4，第一個字符是 'A'，最後一個字符是 'G'
    if len(seq) != 4 or seq[0] != 'A' or seq[-1] != 'G':
        return False
    # 第二個和第三個字符必須在 'E' 到 'T' 之間，且不相同
    return seq[1] in 'EFGHIJKLMNOPQRST' and seq[2] in 'EFGHIJKLMNOPQRST' and seq[1] != seq[2]

def findGen(startTag, endTags, dna):
    length = len(dna)
    startIndex = dna.find(startTag) + 3 # 基因前面是 startTag 'ATG'，加上3移到基因開始的位置
    endIndex = length + 1 # 初始化結束點為超出範圍
    # 遍歷 DNA 字串，尋找符合模式的序列
    for i in range(len(dna) - 3):
        if matches_pattern(dna[i:i+4]):
            # 找到符合模式的序列後，設定基因的起始索引
            startIndex = i + 4
            break
    # 遍歷所有終止標籤，找出最小的符合終止條件的索引
    for tag in endTags:
        endTemp = dna.find(tag, startIndex)
        if endTemp != -1 and endTemp < endIndex:
            endIndex = endTemp
    # 如果沒有找到有效的終止標籤或起始索引不正確，返回默認值
    if endIndex == length + 1 or startIndex < 3:
        return 0, 0, 'None'
    # 提取基因序列
    gen = dna[startIndex:endIndex]
    # 驗證基因序列是否符合條件
    if check(gen):
        return 1, endIndex + 3, gen
    return 2, startIndex + 3, 'None'

def finAllGen(fTag, bTag, dna):
    i, count = 0, 0
    ans = []
    maxlen = 0
    while True:
        dna = dna[i:] # 繼續在剩餘的 DNA 中尋找基因
        b, i, gen = findGen(fTag, bTag, dna) # b=1 表示找到基因，i 更新為下一次查找的起始索引
        if b == 1:
            ans.append(gen) # 添加找到的基因
            maxlen = max(maxlen, len(gen)) # 更新最大基因長度
            count += 1 # 增加找到的基因數量
        elif b == 0: # 沒有找到更多基因
            break
    ans.sort() # 將基因排序
    if count > 0: # 如果找到基因
        for i in range(0, maxlen + 1):
            for j in ans:
                if len(j) == i:
                    print(j) # 按長度順序輸出基因
    elif count == 0: # 如果完全沒找到基因
        print('No gene')

# 讀取起始標籤
fTag = input()
# 讀取終止標籤，並以空格分隔
bTag = input().split(" ")
# 讀取 DNA 序列
dna = input()

# 查找並輸出所有基因
finAllGen(fTag, bTag, dna)