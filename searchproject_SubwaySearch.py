from aiSearch import *
import math
my_subway = {
    # 1, 2, 3 line
    '215 St': [(40.869444, -73.915279), ['207 St'], ['1']],
    '207 St': [(40.864621, -73.918822), ['215 St', 'Dyckman St (1)'], ['1']],
    'Dyckman St (1)': [(40.860531, -73.925536), ['207 St', '191 St'], ['1']],
    '191 St': [(40.855225, -73.929412), ['Dyckman St (1)', '181 St (1)'], ['1']],
    '181 St (1)': [(40.849505, -73.933596), ['191 St', '168 St'], ['1']],
    '157 St': [(40.834041, -73.94489), ['168 St', '145 St (1)'], ['1']],
    '145 St (1)': [(40.826551, -73.95036), ['157 St', '137 St - City College'], ['1']],
    '137 St - City College': [(40.822008, -73.953676), ['145 St (1)', '125 St (1)'], ['1']],
    '125 St (1)': [(40.815581, -73.958372), ['137 St - City College', '116 St - Columbia University'], ['1']],
    '116 St - Columbia University': [(40.807722, -73.96411), ['125 St (1)', 'Cathedral Pkwy (1)'], ['1']],
    'Cathedral Pkwy (1)': [(40.803967, -73.966847), ['116 St - Columbia University', '103 St (1)'], ['1']],
    '103 St (1)': [(40.799446, -73.968379), ['Cathedral Pkwy (1)', '96 St (1, 2, 3)'], ['1']],
    'Harlem 148 St': [(40.82388, -73.93647), ['145 St (3)'], ['3']],
    '145 St (3)': [(40.820421, -73.936245), ['Harlem 148 St', '135 St (2, 3)'], ['3']],
    '135 St (2, 3)': [(40.814229,-73.94077), ['145 St (3)', '125 St (2, 3)'], ['2', '3']],
    '125 St (2, 3)': [(40.807754,-73.945495), ['135 St (2, 3)', '116 St (2, 3)'], ['2', '3']],
    '116 St (2, 3)': [(40.798629, -73.941617), ['125 St (2, 3)', '110 St (2, 3)'], ['2', '3']],
    '110 St (2, 3)': [(40.799075, -73.951822), ['116 St (2, 3)', '96 St (1, 2, 3)'], ['2', '3']],
    '96 St (1, 2, 3)': [(40.793919, -73.972323), ['103 St (1)', '86 St (1)'], ['1', '2', '3']],
    '86 St (1)': [(40.788644, -73.976218), ['96 St (1, 2, 3)', '79 St'], ['1']],
    '79 St': [(40.783934, -73.979917), ['86 St (1)', '72 St (1, 2, 3)'], ['1']],
    '72 St (1, 2, 3)': [(40.778453, -73.98197), ['79 St', '66 St - Lincoln Center'], ['1', '2', '3']],
    '66 St - Lincoln Center': [(40.77344, -73.982209), ['72 St (1, 2, 3)', '59 St - Columbus Circle'], ['1']],
    '59 St - Columbus Circle': [(40.768247, -73.981929), ['66 St - Lincoln Center', '50 St (1)', '50 St (C, E)', '7 Av', '72 St (B, C)'], ['A', 'B', 'C', 'D', '1']],
    '50 St (1)': [(40.761728, -73.983849), ['59 St - Columbus Circle', 'Times Sq - 42 St'], ['1']],
    'Times Sq - 42 St': [(40.75529, -73.987495), ['42 St - Port Authority Bus Terminal', '34 St - Penn Station (1, 2, 3)', '50 St (1)', '5 Av', 'Grand Central - 42 St', '34 St - Herald Sq', '34 St - 11 Av', '49 St'], ['N', 'Q', 'R', 'S', '1', '2', '3', '7']],
    '34 St - Penn Station (1, 2, 3)': [(40.750373, -73.991057), ['28 St (1)', 'Times Sq - 42 St'], ['1', '2', '3']],
    '28 St (1)': [(40.747215, -73.993365), ['34 St - Penn Station (1, 2, 3)', '23 St (1)'], ['1']],
    '23 St (1)': [(40.744081, -73.995657), ['28 St (1)', '18 St'], ['1']],
    '18 St': [(40.74104, -73.997871), ['14 St (1, 2, 3)', '23 St (1)'], ['1']],
    '14 St (1, 2, 3)': [(40.737826, -74.000201), ['18 St', 'Christopher St - Sheridan Sq', '6 Av'], ['1', '2', '3']],
    'Christopher St - Sheridan Sq': [(40.733422, -74.002906), ['14 St (1, 2, 3)', 'Houston St'], ['1']],
    'Houston St': [(40.728251, -74.005367), ['Christopher St - Sheridan Sq', 'Canal St (1)'], ['1']],
    'Canal St (1)': [(40.722854, -74.006277), ['Franklin St', 'Houston St'], ['1']],
    'Franklin St': [(40.719318, -74.006886), ['Canal St (1)', 'Chambers St (1, 2, 3)'], ['1']],
    'Chambers St (1, 2, 3)': [(40.715478, -74.009266), ['Franklin St', 'Rector St (1)', 'Park Place'], ['1', '2', '3']],
    'Park Place': [(40.713051, -74.008811), ['Chambers St (1, 2, 3)', 'Chambers St (A, C)', 'World Trade Center', 'Fulton St'], ['2', '3']],
    'Wall St (2, 3)': [(40.706821, -74.0091), ['Fulton St'], ['2', '3']],
    'Rector St (1)': [(40.707513, -74.013783), ['Chambers St (1, 2, 3)', 'South Ferry'], ['1']],
    'South Ferry': [(40.701411, -74.013205), ['Whitehall St South Ferry', 'Rector St (1)'], ['1']],

    # 7 Line
    '34 St - 11 Av': [(40.755882, -74.001910), ['Times Sq - 42 St'], ['7']],

    # A, C, E line
    'Inwood 207 St': [(40.868072, -73.919899), ['Dyckman St (A)'], ['A']],
    'Dyckman St (A)': [(40.865491, -73.927271), ['Inwood 207 St', '190 St'], ['A']],
    '190 St': [(40.859022, -73.93418), ['Dyckman St (A)', '181 St (A)'], ['A']],
    '181 St (A)': [(40.851695, -73.937969), ['190 St', '175 St'], ['A']],
    '175 St': [(40.847391, -73.939704), ['181 St (A)', '168 St'], ['A']],
    '168 St': [(40.840719, -73.939561), ['175 St', '181 St (1)', '163 St - Amsterdam Av', '157 St'], ['A','C','1']],
    '163 St - Amsterdam Av': [(40.836013, -73.939892), ['168 St', '155 St (C)'], ['C']],
    '155 St (C)': [(40.830518, -73.941514), ['163 St - Amsterdam Av', '145 St (A, B, C, D)'], ['C']],
    '155 St (B, D)': [(40.830135, -73.938209), ['145 St (A, B, C, D)'], ['B', 'D']],
    '145 St (A, B, C, D)': [(40.824783, -73.944216), ['155 St (C)', '155 St (B, D)', '135 St (B, C)'], ['A', 'B', 'C', 'D']],
    '135 St (B, C)': [(40.817894, -73.947649), ['145 St (A, B, C, D)', '125 St (A, B, C, D)'], ['B', 'C']],
    '125 St (A, B, C, D)': [(40.817894, -73.947649), ['135 St (B, C)', '116 St (B, C)'], ['A', 'B', 'C', 'D']],
    '116 St (B, C)': [(40.805085, -73.954882), ['125 St (A, B, C, D)', 'Cathedral Pkwy (110 St) (B, C)'], ['B', 'C']],
    'Cathedral Pkwy (110 St) (B, C)': [(40.800603, -73.958161), ['116 St (B, C)', '103 St (B, C)'], ['B', 'C']],
    '103 St (B, C)': [(40.796092, -73.961454), ['Cathedral Pkwy (110 St) (B, C)', '96 St (B, C)'], ['B', 'C']],
    '96 St (B, C)': [(40.791642, -73.964696), ['103 St (B, C)', '86 St (B, C)'], ['B', 'C']],
    '86 St (B, C)': [(40.785868, -73.968916), ['96 St (B, C)', '81 St - Museum of Natural History (B, C)'], ['B', 'C']],
    '81 St - Museum of Natural History (B, C)': [(40.781433, -73.972143), ['86 St (B, C)', '72 St (B, C)'], ['B', 'C']],
    '72 St (B, C)': [(40.775594, -73.97641), ['81 St - Museum of Natural History (B, C)', '59 St - Columbus Circle'], ['B', 'C']],
    '50 St (C, E)': [(40.762456, -73.985984), ['59 St - Columbus Circle', '42 St - Port Authority Bus Terminal', '7 Av'], ['C', 'E']],
    '42 St - Port Authority Bus Terminal': [(40.757308, -73.989735), ['50 St (C, E)', 'Times Sq - 42 St', '34 St - Penn Station (A, C, E)' ], ['A', 'C', 'E']],
    '34 St - Penn Station (A, C, E)': [(40.752287, -73.993391), ['42 St - Port Authority Bus Terminal', '23 St (C, E)'], ['A', 'C', 'E']],
    '23 St (C, E)': [(40.745906, -73.998041), ['34 St - Penn Station (A, C, E)', '14 St (A, C, E, L)'], ['C', 'E']],
    '14 St (A, C, E, L)': [(40.740893, -74.00169), ['W 4 St', '23 St (C, E)', '6 Av'], ['A', 'C', 'E', 'L']],
    'W 4 St': [(40.732338, -74.000495), ['Broadway-Lafayette St', '14 St (A, C, E, L)', '6 Av', 'Spring St (C, E)'], ['A', 'B', 'C', 'D', 'E', 'F', 'M']],
    'Chambers St (A, C)': [(40.714111, -74.008585), ['Park Place', 'Canal St (A, C, E)', 'Fulton St'], ['A', 'C']],
    'Spring St (C, E)': [(40.726227, -74.003739), ['Canal St (A, C, E)', 'W 4 St'], ['C', 'E']],
    'Canal St (A, C, E)': [(40.720824, -74.005229), ['World Trade Center', 'Chambers St (A, C)', 'Spring St (C, E)'], ['A', 'C', 'E']],
    'World Trade Center': [(40.712582, -74.009781), ['Canal St (A, C, E)', 'Park Place'], ['E']],

    # B, D, F, M line
    'Lexington Av/63 St': [(40.764629, -73.966113), ['57 St'], ['F']],
    'Lexington Av/53 St': [(40.757552, -73.969055), ['51 St', '5 Av/53 St'], ['E', 'M']],
    '7 Av': [(40.762862, -73.981637), ['59 St - Columbus Circle', '47-50 Sts - Rockefeller Ctr'], ['B', 'D', 'E']],
    '47-50 Sts - Rockefeller Ctr': [(40.758663, -73.981329), ['7 Av', '42 St - Bryant Pk', '5 Av/53 St', '57 St'], ['B', 'D', 'F', 'M']],
    '57 St': [(40.764664, -73.980658), ['47-50 Sts - Rockefeller Ctr', 'Lexington Av/63 St'], ['F']],
    '42 St - Bryant Pk': [(40.754222, -73.984569), ['47-50 Sts - Rockefeller Ctr', '34 St - Herald Sq', '5 Av'], ['B', 'D', 'F', 'M']],
    '34 St - Herald Sq': [(40.749567, -73.98795), ['42 St - Bryant Pk', '23 St (F, M)', 'Times Sq - 42 St', '28 St (N, R)'], ['B', 'D', 'F', 'M', 'N', 'Q', 'R']],
    '23 St (F, M)': [(40.742878, -73.992821), ['34 St - Herald Sq', '6 Av'], ['F', 'M']],
    '6 Av': [(40.738228, -73.996209), ['23 St (F, M)', 'W 4 St', '14 St (1, 2, 3)', '14 St (A, C, E, L)', '14 St - Union Sq'], ['F', 'M', 'L']],
    'Broadway-Lafayette St': [(40.725297, -73.996204), ['Bleeker St', '2 Av', 'W 4 St', 'Grand St'], ['B', 'D', 'F', 'M']],
    '2 Av': [(40.723402, -73.989938), ['Essex St', 'Broadway-Lafayette St'], ['F']],
    'East Broadway': [(40.713715, -73.990173), ['Essex St'], ['F']],
    'Essex St': [(40.718315, -73.987437), ['Bowery St', 'East Broadway', '2 Av'], ['F', 'J', 'M', 'Z']],
    'Grand St': [(40.718267,-73.993753), ['Broadway-Lafayette St'], ['B', 'D']],

    # L line
    '3 Av': [(40.732849, -73.986122), ['1 Av', '14 St - Union Sq'], ['L']],
    '1 Av': [(40.730953, -73.981628), ['3 Av'], ['L']],

    # N, Q, R Line
    'Lexington Av/59 St': [(40.76266, -73.967258), ['5 Av/59 St', '59 St'], ['N', 'Q', 'R']],
    '5 Av/53 St': [(40.760167, -73.975224), ['47-50 Sts - Rockefeller Ctr', 'Lexington Av/53 St'], ['E', 'M']],
    '5 Av/59 St': [(40.764811, -73.973347), ['Lexington Av/59 St', '57 St - 7 Av'], ['N', 'Q', 'R']],
    '57 St - 7 Av': [(40.764664, -73.980658), ['5 Av/59 St', '49 St'], ['N', 'Q', 'R']],
    '49 St': [(40.759901, -73.984139), ['Times Sq - 42 St', '57 St - 7 Av'], ['N', 'Q', 'R']],
    '28 St (N, R)': [(40.745494, -73.988691), ['34 St - Herald Sq', '23 (N, R)'], ['N', 'R']],
    '23 (N, R)': [(40.741303, -73.989344), ['28 St (N, R)', '14 St - Union Sq'], ['N', 'R']],
    '8 St - NYU': [(40.730328, -73.992629), ['Prince St', '14 St - Union Sq'], ['N', 'R']],
    'Prince St': [(40.724329, -73.997702), ['Canal St (J, N, Q, R, Z, 6)', '8 St - NYU'], ['N', 'R']],
    'Canal St (J, N, Q, R, Z, 6)': [(40.719527, -74.001775), ['City Hall', 'Prince St', 'Spring St (6)', 'Brooklyn Bridge - City Hall', 'Chambers St (J, Z)', 'Bowery St'], ['J', 'N', 'Q', 'R', 'Z', '6']],
    'City Hall': [(40.713282, -74.006978), ['Canal St (J, N, Q, R, Z, 6)', 'Courtlandt St'],['R']],
    'Courtlandt St': [(40.710668, -74.011029), ['City Hall', 'Rector St (R)'], ['R']],
    'Rector St (R)': [(40.70722, -74.013342), ['Courtlandt St', 'Whitehall St South Ferry'], ['R']],
    'Whitehall St South Ferry': [(40.703087, -74.012994), ['Rector St (R)', 'South Ferry'], ['R', '1']],

    # 4, 5, 6 Line
    '125 St (4, 5, 6)': [(40.804138, -73.937594), ['116 St (6)'], ['4', '5', '6']],
    '116 St (6)': [(40.798629, -73.941617), ['125 St (4, 5, 6)', '110 St (6)'], ['6']],
    '110 St (6)': [(40.79502, -73.94425), ['116 St (6)', '103 St (6)'], ['6']],
    '103 St (6)': [(40.7906, -73.947478), ['110 St (6)', '96 St (6)'], ['6']],
    '96 St (6)': [(40.785672, -73.95107), ['103 St (6)', '86 St (4, 5, 6)'], ['6']],
    '86 St (4, 5, 6)': [(40.779492, -73.955589), ['96 St (6)', '77 St'], ['4', '5', '6']],
    '77 St': [(40.77362, -73.959874), ['86 St (4, 5, 6)', '68 St - Hunter College'], ['6']],
    '68 St - Hunter College': [(40.768141, -73.96387), ['77 St', '59 St'], ['6']],
    '59 St': [(40.641362, -74.017881), ['Lexington Av/59 St', '68 St - Hunter College'], ['4', '5', '6']],
    '51 St': [(40.757107, -73.97192), ['Lexington Av/53 St', '59 St', 'Grand Central - 42 St'], ['6']],
    'Grand Central - 42 St': [(40.752769, -73.979189), ['5 Av', '51 St', '33 St'], ['S', '4', '5', '6', '7']],
    '5 Av': [(40.753821, -73.981963), ['42 St - Bryant Pk', 'Grand Central - 42 St'], ['7']],
    '33 St': [(40.746081, -73.982076), ['Grand Central - 42 St', '28 St (6)'], ['6']],
    '28 St (6)': [(40.74307, -73.984264), ['33 St', '23 St (6)'], ['6']],
    '23 St (6)': [(40.739864, -73.986599), ['28 St (6)', '14 St - Union Sq'], ['6']],
    '14 St - Union Sq': [(40.734673, -73.989951), ['23 St (6)', 'Astor Pl', '23 (N, R)', '8 St - NYU','3 Av','6 Av'], ['L', 'N', 'Q', 'R', '4', '5', '6']],
    'Astor Pl': [(40.730054, -73.99107), ['Bleeker St', '14 St - Union Sq'],['6']],
    'Bleeker St': [(40.725915, -73.994659), ['Spring St (6)', 'Astor Pl', 'Broadway-Lafayette St'], ['6']],
    'Spring St (6)': [(40.722301, -73.997141), ['Bleeker St', 'Canal St (J, N, Q, R, Z, 6)'], ['6']],
    'Brooklyn Bridge - City Hall': [(40.713065, -74.004131), ['Fulton St', 'Chambers St (J, Z)', 'Canal St (J, N, Q, R, Z, 6)'], ['4', '5', '6']],
    'Fulton St': [(40.710368, -74.009509), ['Brooklyn Bridge - City Hall', 'Chambers St (J, Z)', 'Wall St (2, 3)', 'Park Place', 'Wall St (4, 5)'], ['A', 'C', 'J', 'Z', '2', '3', '4', '5', '6']],
    'Wall St (4, 5)': [(40.707557, -74.011862), ['Bowling Green', 'Fulton St'], ['4', '5']],
    'Bowling Green': [(40.704817, -74.014065), ['Wall St (4, 5)'], ['4', '5']],

    # J, Z Line
    'Broad St': [(40.706476, -74.011056), ['Fulton St'], ['J', 'Z']],
    'Chambers St (J, Z)': [(40.713243, -74.003401), ['Fulton St', 'Brooklyn Bridge - City Hall', 'Canal St (J, N, Q, R, Z, 6)'], ['J', 'Z']],
    'Bowery St': [(40.72028, -73.993915), ['Canal St (J, N, Q, R, Z, 6)', 'Essex St'], ['J', 'Z']],

}
express={#A express
                '168 St': [(40.840719, -73.939561), ['145 St (A, B, C, D)'], ['A','C','1']],
                '145 St (A, B, C, D)': [(40.824783, -73.944216), ['168 St', '125 St (A, B, C, D)'], ['A', 'B', 'C', 'D']],
                '125 St (A, B, C, D)': [(40.817894, -73.947649), ['145 St (A, B, C, D)', '59 St - Columbus Circle'], ['A', 'B', 'C', 'D']],
                '59 St - Columbus Circle': [(40.768247, -73.981929), ['125 St (A, B, C, D)', '42 St - Port Authority Bus Terminal'], ['A', 'B', 'C', 'D', '1']],
                '42 St - Port Authority Bus Terminal': [(40.757308, -73.989735), ['59 St - Columbus Circle',], ['A', 'C', 'E']],
                '34 St - Penn Station (A, C, E)': [(40.752287, -73.993391), ['14 St (A, C, E, L)'], ['A', 'C', 'E']],
                '14 St (A, C, E, L)': [(40.740893, -74.00169), ['34 St - Penn Station (A, C, E)'], ['A', 'C', 'E', 'L']],
                'W 4 St': [(40.732338, -74.000495), ['Canal St (A, C, E)', '42 St - Bryant Pk'], ['A', 'B', 'C', 'D', 'E', 'F', 'M']],
                'Canal St (A, C, E)': [(40.720824, -74.005229), ['W 4 St'], ['A', 'C', 'E']],
                #2,3 express
                '96 St (1, 2, 3)': [(40.793919, -73.972323), ['72 St (1, 2, 3)'], ['1', '2', '3']],
                '72 St (1, 2, 3)': [(40.778453, -73.98197), ['96 St (1, 2, 3)', 'Times Sq - 42 St'], ['1', '2', '3']],
                'Times Sq - 42 St': [(40.75529, -73.987495), ['72 St (1, 2, 3)'], ['N', 'Q', 'R', 'S', '1', '2', '3', '7']],
                '34 St - Penn Station (1, 2, 3)': [(40.750373, -73.991057), ['14 St (1, 2, 3)'], ['1', '2', '3']],
                '14 St (1, 2, 3)': [(40.737826, -74.000201), ['34 St - Penn Station (1, 2, 3)', 'Chambers St (1, 2, 3)'], ['1', '2', '3']],
                'Chambers St (1, 2, 3)': [(40.715478, -74.009266), ['14 St (1, 2, 3)'], ['1', '2', '3']],
                # D express
                '42 St - Bryant Pk': [(40.754222, -73.984569), ['W 4 St'], ['B', 'D', 'F', 'M']],
                # 4,5 express
                '125 St (4, 5, 6)': [(40.804138, -73.937594), ['86 St (4, 5, 6)'], ['4', '5', '6']],
                '86 St (4, 5, 6)': [(40.779492, -73.955589), ['125 St (4, 5, 6)', '59 St'], ['4', '5', '6']],
                '59 St': [(40.641362, -74.017881), ['86 St (4, 5, 6)', 'Grand Central - 42 St' ], ['4', '5', '6']],
                'Grand Central - 42 St': [(40.752769, -73.979189), ['59 St', '14 St - Union Sq'], ['S', '4', '5', '6', '7']],
                '14 St - Union Sq': [(40.734673, -73.989951), ['Grand Central - 42 St', 'Brooklyn Bridge - City Hall', '34 St - Herald Sq', 'Canal St (J, N, Q, R, Z, 6)'], ['L', 'N', 'Q', 'R', '4', '5', '6']],
                'Brooklyn Bridge - City Hall': [(40.713065, -74.004131), ['14 St - Union Sq'], ['4', '5', '6']],
                # Q express
                '34 St - Herald Sq': [(40.749567, -73.98795), ['14 St - Union Sq'], ['B', 'D', 'F', 'M', 'N', 'Q', 'R']],
                'Canal St (J, N, Q, R, Z, 6)': [(40.719527, -74.001775), ['14 St - Union Sq'], ['J', 'N', 'Q', 'R', 'Z', '6']]

        }

class SUBwayGraph (GraphNode):
    def __init__(self,location,trainLine):#name/train lline
        GraphNode.__init__(self)     ### my perameter for my graphnode is its current location
        self.location = location     ### lastly what train is at the station
        self.trainLine = trainLine

    def prettyPrint(self):
        print " --- "
        print "Current Location =" + str(self.location) ### keep updateding the user after they move from node to node
        print "Current Train Line" + str(self.trainLine)### letting them know what path they are taking
        print " --- "
        print "\n"

    def __eq__(self, other):   ### comparing 2 noodes to see if they are equal to each other to see if they can move on to the frige
        if self.location == other.location and self.trainLine == other.trainLine:
            return True

        return False

class SubwaySearch(AStarSearch):### call the A star search
    def __init__(self, graphsearch):
        AStarSearch.__init__(self, graphsearch,True)
        self.goalState = SUBwayGraph(goal, my_subway[goal][2]) ### stating goal

    def expand(self,GraphNode): ### return a list of all possible connections related to current graph node AS A NODE
        newstateList=[]
        if('A' or '2' or '3' or '4' or '5' or 'D' or 'Q' in GraphNode.trainLine):### check to see if there is any express train at the station
            if(express.has_key(GraphNode.location)):                             ### checks  to see if express dictionary has key
                    for b in express[GraphNode.location][1]:                     ### add express node to list to  be worked on
                     newstateList.append(SUBwayGraph(b, my_subway[b][2]))

        for a in my_subway[GraphNode.location][1]:               ###add all adjcent connection of current graphnode
            newlist=(SUBwayGraph(a, my_subway[a][2]))
            newstateList.append(newlist)                        ### adds nodes to list to be worked on
        return  newstateList

    def goalTest(self,GraphNode):### compares the graphnode and what the user input as the goal by the name of the train station and
        if (GraphNode == self.goalState):### avliable train line at that station
            return True
        return False

    def heuristic(self,GraphNode):### The heuristic  is the distance foumula D= sqrt((x2-x1)^2+(y2-y1)^2) the distance between two node
        heur = 0.00000000000      ### this will show the shortest station to the goal.

        heur = math.sqrt((my_subway[goal][0][0] - my_subway[GraphNode.location][0][0]) ** 2+(my_subway[goal][0][1] - my_subway[GraphNode.location][0][1]) ** 2)

        return heur


    def cost(self,GraphNode1,GraphNode2):# return a cost of 1 for every
        return 1

start=input('(ex: ''\'Bowery St\''' )start:')            ###<----  input method for start and goal for running program
goal=input('(ex: ''\'Chambers St (J, Z)\''' )goal:')     ###<---- CAREFULL TO TYPE STRING EXactly LIKE  THE STRING IN my_subway dictionary
                                                         ###       """""""""""""""""OR comment out and """"""""""""""""""
#start='145 St (A, B, C, D)'           ### <---------------------------------------  USE direct input
#goal='Times Sq - 42 St'               ### <---------------------------------------  USE direct input


SUBway=SubwaySearch(True)
startNode =SUBwayGraph(start, my_subway[start][2])
SUBway.search(startNode)