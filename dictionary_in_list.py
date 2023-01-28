travel_log=[ {"county":"banglasesh",
              "visited":"1,2",
              "city":["dhaka","mymenshingh","nowakhali"]


},

             {
                 "county":"india",
                 "visited":"1,2,3",
                 "city":["kolikata","mumbai","rajisthan" ]


             },

]
def add_new_county (visited_county,new_visited,visited_citys):
    new_county={}

    new_county["county"]=visited_county
    new_county["visited"]=new_visited
    new_county["city"]=visited_citys

    travel_log.append(new_county)




add_new_county(visited_county="russia",new_visited=2,visited_citys=["moscow","perent"])

print(travel_log)