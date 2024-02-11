import collections
  
class determine:
    def __init_subclass__(self):
        (lambda: print(collections._collections_abc.generator.gi_code))()
        (lambda: print(collections._collections_abc.async_generator.asend))()
        try:
            collections.ChainMap.new_child(self)
        except:
            print("accepted")
class tint(determine):
    def __init__(self):
        super(tint, self).__init__()
tint()
        