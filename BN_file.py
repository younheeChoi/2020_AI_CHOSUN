import pickle
import pandas as pd
import glob
import numpy as np

# 비어있는거 만들고 파라메타 정의(뭘 뽑아올건지 목록)
train_x, train_y = [], []
PARA = ['UAVLEG1', 'UAVLEG2', 'UAVLEG3', 'ZINST58', 'ZINST75', 'ZINST73', 'ZINST74','ZINST30', 'ZINST78',
        'WFWLN1', 'WFWLN2', 'WFWLN3', 'ZINST26', 'ZINST22', 'BFV122','URHXUT','ZINST56','KBCDO23',
        'ZINST65', 'ZINST22', 'DSECON', 'WSTM1', 'WSTM2', 'WSTM3', 'KFAST', 'KSLOW','BPORV',
        'UNRHXUT','WFPLN1','WFPLN2','WFPLN3','WTIN','BFV499', 'BFV489', 'BFV479'] #30
# DB에서 모든 파일 다 붙이고 나면 종료
for one_file in glob.glob('DB/*.csv'):
    LOCA = pd.read_csv(one_file)
    if len(train_x) == 0:
        train_x = LOCA.loc[:, PARA].to_numpy()
        train_y = LOCA.loc[:, ['Accident_nub']].to_numpy()
    else:
        get_x = LOCA.loc[:, PARA].to_numpy()
        get_y = LOCA.loc[:, ['Accident_nub']].to_numpy()
        train_x = np.vstack((train_x, get_x))
        train_y = np.vstack((train_y, get_y))


total_Data=[train_x,train_y]

with open('Data_file.bin','wb') as file:
    pickle.dump(total_Data,file)

with open('Data_file.bin','rb') as file:
    total_Data = pickle.load(file)

print(np.shape(total_Data[0]))