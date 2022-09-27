def lerp(start,goal,alpha):  #[L]inear int[ERP]olation function
  return start + (goal - start) * alpha
  
class vector2:
  x = 0
  y = 0
  def __init__(self, x, y):
      self.x = -(x-200)
      self.y = -(y-200)

class questions:
  def __init__(self):
    return
  #def new(self,information):
    #return(len(self))
    
  
shapes = {
    "rhombus": {
        "position": vector2(300,150),
        "sides": 4,
        "color": "red",
        "fillamount": 360
    },
    "circle": {
        "position": vector2(100,150),
        "color": "blue",
        "fillamount": 360,
        "sides": 0      #here to debug the test case
    },
    "pentagon": {
        "position": vector2(100,350),
        "sides": 5,
        "color": "green",
        "fillamount": 360
    },
    "halfcircle": {
        "position": vector2(300,350),
        "color": "yellow",
        "fillamount": 180
    },
}
 
 
 
# for shapename in shapes:
#     shape = shapes[shapename]
#     setposition(shape["position"].x,shape["position"].y)
#     color(shape["color"])
#     pendown()
#     begin_fill()
#     if hasKey(shape,"sides"):
#         if shape["sides"] == 0:      #here to debug the test case because it just wouldn't work otherwise
#             circle(shape_radius)
#         else:
#             circle(shape_radius,shape["fillamount"],shape["sides"])
#     else:
#         circle(shape_radius,shape["fillamount"])
#     if shapename == "halfcircle":
#         left(180)
#     penup()
#     end_fill()
#     print(shapename,":",shape["position"].x,shape["position"].y)