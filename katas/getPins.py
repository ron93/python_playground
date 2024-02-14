pad = """
   
123
   
456
   
789
   
 0 
    
    
"""

    

def get_pins(observed):
  if len(observed)==1:
      loc = pad.find(observed)
      print(loc)
      opts = [loc, loc+1, loc-1, loc+8, loc-8]
      print(f"opts{opts}")
    #   for l in opts:
    #      print(l)
    #      if pad[l].strip():
    #         print(f" {l} pad[l] {pad[l]}")
      return [pad[l] for l in opts if pad[l].strip()]
  else:
      return [l+r for l in get_pins(observed[0]) for r in get_pins(observed[1:])]

print(get_pins('1'))