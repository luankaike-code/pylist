def component_fac(dad_class: type) -> type:
  class Component(dad_class):
    def __init__(self, root, **args):
      super().__init__(root, **args)

    def constructor(self):
      pass

    def update(self):
      self.constructor()

  return Component