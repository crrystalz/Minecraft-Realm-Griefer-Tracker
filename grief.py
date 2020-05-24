import os
import json

#Change this to the path to your MOST RECENT realm world download
path = r'C:\Users\saswa\AppData\Roaming\.minecraft\saves\Realm Of The Crystal Clan (World 2)-3'

path2 = r'C:\Users\saswa\AppData\Roaming\.minecraft\saves\Realm Of The Crystal Clan (World 2)-2'

statsDir = path + "\stats"

def findStats():
    for filename in os.listdir(statsDir):
        with open(os.path.join(statsDir, filename)) as json_file:
            data = json.load(json_file)
            used = (data['stats']['minecraft:used'])
            
            fireworks = 0
            tnt = 0
            creeperHeads = 0
            soulsand = 0
            for key in used:
                if key == "minecraft:firework_rocket":
                    fireworks += used[key]

                if key == "minecraft:creeper_head":
                    creeperHeads += used[key]

                if key == "minecraft:tnt":
                    tnt += used[key]

                if key == "minecraft:soul_sand":
                    tnt += used[key]

            #print("Fireworks: " + str(fireworks)) 
            print(str(filename) + ":")
            print("")
            print("TNT: " + str(tnt))
            print("Creeper Heads: " + str(creeperHeads))
            print("Soul Sand: " + str(soulsand))
            print("")
            #jstr = json.dumps(data, indent=4)
            #print(jstr)

findStats()