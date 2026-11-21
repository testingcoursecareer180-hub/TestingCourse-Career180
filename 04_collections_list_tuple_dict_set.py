"""
Lesson 4 — list, tuple, dict, and set

list  : ordered, and you can change it
tuple : ordered, and it stays fixed
dict  : look up a value by a name
set   : each value is stored once
"""
#By moahmed Farghali

my_list  = ["a", "b", "a"]          # list: ['a', 'b', 'a']   (التكرار مسموح)
my_tuple = ("a", "b", "a")          # tuple: نفس الشيء لكن ثابت ,لا يتم اضافة او حذف او تعديل
my_dict  = {"first": "a", "second": "b"}   # dict: أصل للقيمة بالاسم
my_set   = {"a", "b", "a"}          # set: {'a', 'b'}  (التكرار اختفى)

print(my_list[0])        # a      الوصول بالرقم
print(my_dict["second"]) # b      الوصول بالاسم
print(my_set)            # {'a', 'b'}   لا ترتيب مضمون

my_list[0] = "z"         # ✅ يعمل
# my_tuple[0] = "z"      # ❌ خطأ TypeError لأن tuple ثابت
# my_set[0]              # ❌ خطأ لأن set ليس له index

#Tuple to List and List to Tuple
viewport = (1920, 1080)
temp = list(viewport)    # [1920, 1080]
temp.append(500)         # الآن يمكن الإضافة
viewport = tuple(temp)   # (1920, 1080, 500)


# list: append تضيف في آخر القائمة
browsers = ["chrome", "firefox"]
browsers.append("edge")
print(browsers)        # ['chrome', 'firefox', 'edge']

# set: add تضيف قيمة، وإذا كانت موجودة لا يحدث شيء
statuses = {"passed", "failed"}
statuses.add("skipped")
statuses.add("passed")  # موجودة أصلاً، لا تتكرر
print(statuses)        # {'passed', 'failed', 'skipped'} (الترتيب قد يختلف)

# dict: تضيف بتحديد المفتاح
user = {"name": "Mona"}
user["role"] = "admin"
print(user)            # {'name': 'Mona', 'role': 'admin'}