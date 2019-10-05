import sys

args=sys.argv[1:]

data_type=['Students','Name','Midterm','Final','Average','Grade']

def show(data_dict_list):
    data_dict_list.sort(key=lambda x:x['Average'],reverse=1)

    print('Students\tName\t\tMidterm\tFinal\tAverage\tGrade')
    print('-'*60)
    for idx in range(len(data_dict_list)):
        print('%s\t%s\t%s\t%s\t%.1f\t%s' %tuple(data_dict_list[idx].values()))

def Cal_average_grade(data_dict):
    data_dict['Students']=int(data_dict['Students'])
    data_dict['Midterm']=float(data_dict['Midterm'])
    data_dict['Final']=float(data_dict['Final'])

    data_dict['Average']=float((data_dict['Midterm']+data_dict['Final'])/2)
    if data_dict['Average'] >= 90:
        data_dict['Grade']='A'
    elif data_dict['Average'] >= 80:
        data_dict['Grade']='B'
    elif data_dict['Average'] >= 70:
        data_dict['Grade']='C'
    elif data_dict['Average'] >= 60:
        data_dict['Grade']='D'
    else:
        data_dict['Grade']='E'
    return data_dict

def search(data_dict,input_x):
    searched_dict=list()
    for d in data_dict:
        if input_x==d['Students']:
            searched_dict.append(d)
            return searched_dict

def Load_data(data_dict1):
    f=open('students.txt','r')
    while 1:
        data0=f.readline()
        if data0!='':
            data1=data0.strip().split('\t')
            data_dict0=dict(zip(data_type,data1))
            data_dict1.append(Cal_average_grade(data_dict0))
        else:
            f.close()
            break

#----------------
data_dict1=list()
Load_data(data_dict1)



keeprun=1
while keeprun:
    command=input()
    if command=='show':
        show(data_dict1)
    elif command=='quit':
        keeprun=0
    elif command=='search':
        input_x=int(input('enter the student number to search'))
        show(search(data_dict1,input_x))
