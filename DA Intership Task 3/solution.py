# 1 st question
def each_word_frequency(text):
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq


# 2nd question

def each_character_frequency(text):
    freq={}
    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

# 3rd question
def non_repeating_character(text):
    freq={}
    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in freq:
        if freq[ch]==1:
            return ch
            break

# 4th question
def anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        freq1={}
        freq2={}
        for ch in s1:
            if ch in freq1:
                freq1[ch]+=1
            else:
                freq1[ch]=1
        for ch in s2:
            if ch in freq2:
                freq2[ch]+=1
            else:
                freq2[ch]=1
    if freq1 == freq2:
        return True
    else:
        return False


# 5th question
def first_repeating_character(text):
    seen=set()
    for ch in text:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

# 6th question
def all_zero_to_end(num):
    non_zero=[]
    for i in num:
        if i!=0:
            non_zero.append(i)
    zero_count=len(num)-len(non_zero)
    result=non_zero+[0]*zero_count

    return result

# 7th question
def second_highest_distinct(num):
    largest_num=num[0]
    second_num=num[0]
    found=False
    for i in num:
        if i > largest_num:
            second_num=largest_num
            largest_num = i
            found=True

        elif i < largest_num:
            if not found or i > second_num:
                second_num = i
                found=True
    if found:
        return second_num
    else:
        return "No second highest number"

# 8th question
def remove_duplicates(num):
    unique_num=[]
    for i in num:
        if i not in unique_num:
            unique_num.append(i)
    return unique_num



# 9th question
def missing_numbers(num,n):
    for i in range(1,n+1):
        if i not in num:
            return i

# 10 th question
def two_numbers_sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return num[i],num[j]
    return None



# 11 th question
def closest_to_zero(num):
    closest=num[0]
    for i in num:
        if abs(i)< abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i > closest:
            closest = i
    return closest

# 12 th question
def common_element(l1,l2):
    two_list_common=[]
    for i in l1:
        for j in l2:
            if i == j:
                two_list_common+=[i]
                break
    return two_list_common


#13th question
def rotate_right(nums,k):
    k=k%len(nums)
    return nums[-k:]+nums[:-k]


# 14 th question
def max_sum_consective(nums):
    max_sum=nums[0]+nums[1]
    for i in range(1,len(nums)-1):
        current_sum=nums[i]+nums[i+1]

        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# 15 th question

def all_pairs_equal_numbers(nums,target):
    pairs=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                pairs+= [(nums[i],nums[j])]
    return pairs
