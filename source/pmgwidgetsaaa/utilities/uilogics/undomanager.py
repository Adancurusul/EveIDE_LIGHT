"""
用于撤销和重做的数据结构。

"""

from typing import Any


class Stack():
    def __init__(self, stack_size: int = 10):
        self.pointer: int = 0
        self.content = []
        self.stack_size = stack_size

    def push(self, obj):
        self.content.append(obj)

    def pop(self):
        self.content.pop()


class UndoManager():
    """
    用于撤销和重做的管理类
    """

    def __init__(self, stack_size: int = 10):
        self.pointer: int = 0
        self.content = []
        self.stack_size = stack_size

    def push(self, obj:Any):
        """
        压栈时指向栈顶，这里就是撤销时候的逻辑。
        :param obj:
        :return:
        """
        if self.pointer < len(self.content) - 1:
            self.pointer += 1
            self.content[self.pointer] = obj
        else:
            self.content.append(obj)
            self.pointer = len(self.content) - 1
            if len(self.content) > self.stack_size:
                self.content.pop(0)

    def undo(self) -> Any:
        if 0 < self.pointer <= len(self.content) - 1:

            obj = self.content[self.pointer]
            self.pointer -= 1
            return obj
        else:
            if len(self.content) > 0:
                self.pointer = 0
                return self.content[0]
            else:
                return None

    def redo(self) -> Any:
        if 0 <= self.pointer < len(self.content) - 1:
            self.pointer += 1
            return self.content[self.pointer]
        else:
            if len(self.content) > 0:
                self.pointer = len(self.content) - 1
                return self.content[self.pointer]
            else:
                return None

    def last_value(self)->Any:
        try:
            return self.content[self.pointer]
        except:
            return None

    def __len__(self):
        return len(self.content)


if __name__ == '__main__':
    manager = UndoManager()
    manager.push('a')
    manager.push('ab')
    manager.push('abc')
    manager.push('ab')
    manager.push('abd')
    manager.push('abde')
    manager.push('abdef')
    manager.push('abdefg')
    print(manager.content, manager.pointer, len(manager))
    print(manager.undo(), manager.pointer, len(manager))
    print(manager.undo(), manager.pointer, len(manager))
    manager.push('abdefgh')
    manager.push('abdefghi')
    manager.push('abdefghij')
    manager.push('abdefghijk')
    manager.push('abdefghijkl')
    manager.push('abdefghijklm')
    print(manager.content)
    print(manager.undo())
    print(manager.undo())
    print(manager.redo())
    print(manager.redo())
