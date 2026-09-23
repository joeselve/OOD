def bubblesort(m_list):
    for i in range(len(m_list)):
        for j in range(len(m_list) - i - 1):
            if m_list[j] > m_list[j+1]:
                m_list[j+1], m_list[j] = m_list[j], m_list[j+1]
    return m_list

def check(m_list):
    for i in range(len(m_list) - 1):
        if m_list[i] > m_list[i + 1]:
            return False
    return True

inp = [int(i) for i in input("Enter Input : ").split()]

if check(inp):
    print("Yes")
else:
    print("No")
