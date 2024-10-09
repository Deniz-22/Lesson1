grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st = (list(students))
st1 = st.sort()
print(st)
average1 = sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4])
average2 = sum([2, 2, 2, 3])/len([2, 2, 2, 3])
average3 = sum([4, 5, 5, 2])/len([4, 5, 5, 2])
average4 = sum([4, 4, 3])/len([4, 4, 3])
average5 = sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])
print(average1,average2,average3,average4,average5)
print((st[0:2:2],average1),(st[1:2:2],average2),(st[2:3:3],average3),(st[3:4:4],average4),(st[4:5:5],average5))
