import lehd
import pandas as pd
import geopandas as gpd

state_codes = [["AL","01"],["AK","02"],["AS","60"],["","03"],["AZ","04"],["AR","05"],["BI","81"],["CA","06"],["","07"],["CO","08"],["CT","09"],["DE","10"],["DC","11"],["FL","12"],["FM","64"],["GA","13"],["","14"],["GU","66"],["HI","15"],["HI","84"],["ID","16"],["IL","17"],["IN","18"],["IA","19"],["JI","86"],["JA","67"],["KS","20"],["KY","21"],["KR","89"],["LA","22"],["ME","23"],["MH","68"],["MD","24"],["MA","25"],["MI","26"],["MI","71"],["MN","27"],["MS","28"],["MO","29"],["MT","30"],["NI","76"],["NE","31"],["NV","32"],["NH","33"],["NJ","34"],["NM","35"],["NY","36"],["NC","37"],["ND","38"],["MP","69"],["OH","39"],["OK","40"],["OR","41"],["PW","70"],["PA","95"],["PA","42"],["","43"],["PR","72"],["RI","44"],["SC","45"],["SD","46"],["TN","47"],["TX","48"],["UM","74"],["UT","49"],["VT","50"],["VA","51"],["","52"],["VI","78"],["WI","79"],["WA","53"],["WV","54"],["WI","55"],["WY","56"]]

state_codes = [["CT","09"],["DE","10"],["DC","11"],["FL","12"],["FM","64"],["GA","13"],["","14"],["GU","66"],["HI","15"],["HI","84"],["ID","16"],["IL","17"],["IN","18"],["IA","19"],["JI","86"],["JA","67"],["KS","20"],["KY","21"],["KR","89"],["LA","22"],["ME","23"],["MH","68"],["MD","24"],["MA","25"],["MI","26"],["MI","71"],["MN","27"],["MS","28"],["MO","29"],["MT","30"],["NI","76"],["NE","31"],["NV","32"],["NH","33"],["NJ","34"],["NM","35"],["NY","36"],["NC","37"],["ND","38"],["MP","69"],["OH","39"],["OK","40"],["OR","41"],["PW","70"],["PA","95"],["PA","42"],["","43"],["PR","72"],["RI","44"],["SC","45"],["SD","46"],["TN","47"],["TX","48"],["UM","74"],["UT","49"],["VT","50"],["VA","51"],["","52"],["VI","78"],["WI","79"],["WA","53"],["WV","54"],["WI","55"],["WY","56"]]

for state in state_codes:

    print(state)

    try:
        df = lehd.dl_lodes.od(
            year = 2016,
            geography = "CT",
            type = "JT00",
            origins = [state[1]],
            destinations = [state[1]],
            constrained = "no"
            )

        temp = lehd.to_geo.od(df)

        temp = temp[["geometry","S000"]]

        temp = temp[temp["S000"] > 9]

        temp.to_file("data/state_geojsons/" + state[0] + ".geojson", driver='GeoJSON')

    except:
        None

        print("MEEEEOOOOOOWWWWWWW")




#
#
# print(df)