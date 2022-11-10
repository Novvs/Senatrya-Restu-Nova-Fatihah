#soal 1#
#List= diawali dan diakhiri dengan tanda kurung siku []#
#dictionary= Menggunakan tanda kurawal{},dan datanya tersusun karena dictionary ini mempunyai key dan value#
#tuple= menggunakan tanda kurung biasa()#
#set = menggunakan kurawal juga {}, tetapi tidak tersusun dan jika ada data yang sama maka akan dihapus#

#soal 2#
list = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]

print (list[1:5])

#soal 3#
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
print (a[1] [1:3])
#soal 4#
a = [
    [5, 9, 8],
    [0, 0, 6],
    [5, 9, 10],
    [11, 0, 6]
    ]
print (a [2:4]
)
#soal 5#
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del areas [8:10]
print (areas)
#soal 6#
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x %2 == 0]

print (T)

#soal 7#
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ["itali"] = "roma"
print (europe)
#soal 8#
print (("A" == "a")) and ((10 > 9))
print ((10 == 10)) or ((10 > 11))
print (not ("a" == "a"))
#soal 9#
A = 10000
if A > 100000 :
    print ("High")
elif A > 50000  :
    print ("medium")
elif A <= 50000 :
    print ("low")


























