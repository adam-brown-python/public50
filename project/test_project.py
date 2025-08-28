from project import add,delete,show
def test_add():
   assert add("test_student","0","test") == "student_add"

def test_delete():
    add("test_student","0","test")
    assert delete("test_student","0","test") == "student_delete"

def test_show():
   add("test_student","0","test")
   assert show("test") == "student_show"
