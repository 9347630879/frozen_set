
#workss on sets methods
#interseection_update

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
(names1.intersection_update(names2))
print(names1)
print(names2)

#isdisjoint
names1 = {'A'}
names2 = {'Mahendra','singh','dhoni'}
print(names1.isdisjoint(names2))

#differences

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.difference(names2))

#symmetric_differences
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.symmetric_difference(names2))


#symmetric_differences_update
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
(names1.intersection_update(names2))
print(names1)
print(names2)


#isubset

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'sai'}
print(names2.issubset(names1))


#issuperset


names1 = {'dhoni'}
names2 = {'mahendra','singh','dhoni'}
print(names1.issuperset(names2))


#frozen_methods
#union

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.union(names2))

#intersection


names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.intersection(names2))

#isdisjoint


names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.isdisjoint(names2))

#differences

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.difference(names2))

#symmetric_differences
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.symmetric_difference(names2))

#isubset

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'sai'}
print(names2.issubset(names1))


#issuperset


names1 = {'dhoni'}
names2 = {'mahendra','singh','dhoni'}
print(names1.issuperset(names2))


#dictionary data type

#implicit

userdetails = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(type(userdetails))

#explicit

userdetails = dict({'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'})
print(type(userdetails))

#data variable\annotation

userdetails:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(type(userdetails))

