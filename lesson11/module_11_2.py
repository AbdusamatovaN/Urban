import inspect


def introspection_info(obj):
   d = dict()
   d['type'] = type(obj)
   d['attributes'] = dir(obj)
   d['methods'] = inspect.getmembers(obj, predicate=inspect.ismethod)
   d['module'] = inspect.getmodule(obj)

   return d

number_info = introspection_info(42)
print(number_info)