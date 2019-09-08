# recursive call
def call(list, group1, group2):
    # print(str(list)+", "+str(group1)+", "+str(group2));
    if len(list) == 0:
        return sum(group1) == sum(group2)
    # print(len(list))
    element = list[0];
    newList = list.copy();
    newList.pop(0);

    newGroup1 = group1.copy();
    newGroup1.append(element);
    if call(newList,newGroup1,group2):
        return True;

    newGroup2 = group2.copy();
    newGroup2.append(element);
    if call(newList,group1,newGroup2):
        return True;
    return False;
# program
list = [1,3,2,4,11,14,17,20]; # input list
print(call(list, [], []));
