import os


def TextInputFormat(path: str) -> list:
    '''
    读取路径为path的文件，并将内容按行分割

    输入：
    path - 文件路径

    返回：
    句子列表
    '''

    sentences = []

    with open(path, "r") as f:
        sentences = f.readlines()

    return sentences

def CountOneFile(path: str) -> dict:
    '''
    统计一个文件中的词频

    输入：
    path - 文件路径

    返回：
    词频字典
    '''
    word_list = {}
    sentences = TextInputFormat(path)
    
    for sentence in sentences:
        for word in sentence.split():
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1
    
    return word_list

def Map(folder_name: str) -> list:
    '''
    统计文件夹中所有文件的词频

    输入：
    folder_name - 文件夹名称

    返回：
    每一个文件中的词频
    '''

    WordCounts = []
    file_list = os.listdir(folder_name)
    for file in file_list:
        path = folder_name + '\\' + file
        WordCounts.append(CountOneFile(path))
    return WordCounts

def Reduce(map_result: list) -> dict:
    '''
    合并Map的结果

    输入：
    map的结果列表

    返回：
    合并后的结果
    '''

    Word_Count = {}
    for result in map_result:
        for key, value in result.items():
            if key in Word_Count:
                Word_Count[key] += value
            else:
                Word_Count[key] = value
    return Word_Count


if __name__ == '__main__':
    folder_name = 'hadoop'
    result = Reduce(Map(folder_name))
    print(result)