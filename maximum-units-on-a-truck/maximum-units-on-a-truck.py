class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(
            boxTypes,
            key=lambda x: x[1],
            reverse=True
        )
        total_units = 0
        for boxtype in boxTypes:
            if truckSize == 0:
                return total_units
            number_of_boxes_to_put = min(boxtype[0], truckSize)
            total_units += number_of_boxes_to_put * boxtype[1]
            truckSize -= number_of_boxes_to_put
        return total_units