from array import array
def compute_fence_center(point_list:array):
    if point_list is None or len(point_list) < 1:
        return 0,0
    lat_center = 0
    lng_center = 0
    for point in point_list:
        lat_center += point["latitude"]
        lng_center += point["longitude"]
    lat_center /= len(point_list)
    lng_center /= len(point_list)
    return (lat_center,lng_center)
