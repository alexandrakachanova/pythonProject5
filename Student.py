class Student:

    id = 0
    def __init__(self):
        self.__marks = {}
        self.__id = 0

    def add(self, mark=0, subject=''):
        if subject:
            self.__marks[subject] = mark
        else:
            self.__marks[self.__id] = mark
            self.__id += 1

    def get_mark(self):
        return self.__marks.values

    def get_subjects(self):
        return self.__marks.values()

    def get_marks(self):
        return self.__marks.keys()

if __name__ == '__main__':
    st = Student()
    st.add(10)
    st.add(9)
    st.add(5)
    print(st.get_mark())

