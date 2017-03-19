#!/usr/bin/env python
#######
#
#######
import GUI
import numpy as np
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
####################################################
################# Calculations #####################
####################################################

def find_distance(SH_loc,scen_loc):
    #Finds distance in km given location of superhero [lat,long] and scenario [lat,long]
    R = 6371 #Earth radius in km
    print(SH_loc)
    SH_lat, SH_long = SH_loc[0],SH_loc[1]
    Scen_lat,Scen_long = scen_loc[0],scen_loc[1]
    SH_phi, SH_theta = np.radians(SH_lat), np.radians(SH_long)
    Scen_phi, Scen_theta = np.radians(Scen_lat), np.radians(Scen_long)
    dphi = SH_phi - Scen_phi
    dtheta = SH_theta - Scen_theta
    a = np.sin(dphi/2)**2 + np.cos(SH_phi)*np.cos(Scen_phi)*np.sin(dtheta/2)**2
    c = 2*np.math.atan2(np.sqrt(a), np.sqrt(1-a))
    return R*c

def find_ranking(distance, fraction_desirable_traits):
    #ranking function preferably around range 0-100
    #the lower the distance and higher desirable traits the better
    #return number
    return 1

####################################################
################# SCREEN DISPLAY ###################
####################################################

def gotoscreen1():
    #buttons -> blank apart from button 2 = arrange meeting ##FOR NOW: JUST BLANK##
    #messages, title + world map
    pass

def print_emergency_message(time,description,location):
    #print message on screen including time description and location
    pass

def go_to_location(location):
    #zoom into location on location map or add dot to world map
    pass

def screen3_add_buttons(to_display):
    #look up names and (necessary and) desirable traits of SH_IDs = to_display
    #change first 3 buttons to display these names and traits
    #change 4th button to Send Team
    pass

def screen4_add_buttons():
    #display 4 teams on buttons:
    #1: Avengers
    #2: Justice League
    #3: X-Men
    #4: Team Hacky McHackface
    pass

def deactivate_button(button):
    #change button to deactivated (e.g. change colour to grey)
    pass

def display_message(message_response):
    #find last recieved message. look up name of sender
    #if message_response == 'Y':
    #   display messaage: "name" is on their way!
    #else:
    #   display message: "name" has declined request
    pass

####################################################
################# LEDs #############################
####################################################

def switch_LEDs(bin):
    #bin = list of 4 0s or 1s
    #turn on the LEDs with 1s, off with 0s
    pass

def flash_LEDs():
    for j in range(5):
        time.sleep(.5)
        switch_LEDs(1111)
        time.sleep(.5)
        switch_LEDs(0000)
        j += 1

####################################################
################# CHECKING FOR EVENTS ##############
####################################################

########### Checking for button presses ############

#checks return true if pressed, false if not
def button1check():
    return False

def button2check():
    return False

def button3check():
    return False

def button4check():
    return False

def button5check():
    return False

def button6check():
    return False

def button7check():
    return False


def buttons_check():
    #Return 0 for no button
    #i for button i (i 1 to 7)
    if button1check():
        return 1
    elif button2check():
        return 2
    elif button3check():
        return 3
    elif button4check():
        return 4
    elif button5check():
        return 5
    elif button6check():
        return 6
    elif button7check():
        return 7
    else:
        return 0

######## Checking for emergencies ##################
def emergency_read(message_text):
    #write time received to database
    #write long description to database (from text)
    #write location to database (from text)
    #print message to screen with print_emergency_message(time,description,location)
    #alter location map with go_to_location(location)
    #return 0 if no emergency, emergency ID if emergency
    return False

######## Checking for messages #####################
def message_check():
    # check for received text
    #if message_length > (low number)
    #   emergency_ID = emergency_read(message)
    #elif message_text in ['Y','N']
    #   return message_text
    #else
    #   error
    # return 0 for no message, emergency ID if emergency, 'Y'/'N' if SH response
    return False

####################################################
################# EMERGENCY ########################
####################################################

########### EMERGENCY FINDING HEROES FUNCTIONS ###########

def find_suitable_heroes(emergency_ID):
    #SQL query:
    #Return list of IDs of heroes with necessary traits of given emergency
    return [1,2,3,4,6]

def find_available_heroes(SH_IDs):
    #interface with Chronofy and database to return list of superhero IDs of those available now
    return [1,2,3,6]

def write_distances(SH_IDs):
    #read locations of SHs of SH_IDs from database
    #use find_distance(SH_loc,scen_loc) to find distances
    #write distances to database
    pass

def write_rankings(emergency_ID,SH_IDs):
    #read distances of SH_IDs from emergency_ID
    #find fraction of desirable traits of emergency_ID that match with traits of SH_IDs
    #calculate rankings with find_ranking(distance, fraction_desirable_traits)
    #write rankings to database
    pass

def find_top_3(page):
    ranking_range = range[page*3 - 2:page*3]
    #sort database by rankings
    #return list of SH_IDs of those in ranking range.
    return[2,3,6]

######### SEND A HERO OR TEAM ########################

def send_request(hero_name,hero_phone,emergency_message,emergency_location):
    #send message to hero detailing emergency using info in arguments
    pass

def hero_selected(hero_ID,emergency_ID):
    #get hero name, hero phone number, emergency long message and emergency location from database
    #send_request(hero_name,hero_phone,emergency_message,emergency_location)
    pass

def team_selected(team,emergency_ID):
    #for now summons available team members
    #could later be modded to find the next time they are all free and summon them then
    if team == 1:
        #team_IDs = SQL query for Avengers' IDs
        pass
    if team == 2:
        # team_IDs = SQL query for Justice League's IDs
        pass
    elif team ==3:
        # team_IDs = SQL query for X-Men's IDs
        pass
    else:
        # team_IDs = SQL query for Hacky McHackface's IDs
        pass
    team_IDs = [1,2,3,4] #placeholder

    available_team_IDs = find_available_heroes(team_IDs)

    for hero_ID in available_team_IDs:
        hero_selected(hero_ID,emergency_ID)

    deactivate_button(team)


def send_team(emergency_ID):
    screen4_add_buttons()
    # check for events
    while True:
        button_pressed = buttons_check()
        message_received = message_check()
        if button_pressed in [1, 2, 3, 4]:
            # team seleceted
            team_selected(button_pressed,emergency_ID)
        elif button_pressed == 5:
            # "no (further) action" (/"home") selected
            home_screen()
        elif message_received:
            if message_received in ['Y', 'N']:
                display_message(message_received)
            else:
                display_message(message_received)
                print("another emergency message! can't deal with more than one at a time, sorry!")
    pass

####### MAIN EMERGENCY FUNCTION ######################

def display_page_3(page,emergency_ID):
    #find heroes for this page
    to_display = find_top_3(page)
    # display buttons
    screen3_add_buttons(to_display)
    # check for events
    while True:
        button_pressed = buttons_check()
        message_received = message_check()
        if button_pressed in [1, 2, 3]:
            # hero seleceted
            hero_ID = to_display[button_pressed]
            hero_selected(hero_ID,emergency_ID)
            deactivate_button(button_pressed)
        elif button_pressed == 4:
            # send team selected
            send_team(emergency_ID)
        elif button_pressed == 5:
            # "no (further) action" (/"home") selected
            home_screen()
        elif button_pressed == 6:
            #"back" selected
            if page > 1:
                page -= 1
                display_page_3(page,emergency_ID)
        elif button_pressed == 7:
            # "more" selected
            if page < 6:
                page += 1
                display_page_3(page,emergency_ID)
        elif message_received:
            if message_received in ['Y', 'N']:
                display_message(message_received)
            else:
                display_message(message_received)
                print("another emergency message! can't deal with more than one at a time, sorry!")

def emergency(emergency_ID):
    print('emergency')
    flash_LEDs()
    #filter and rank heroes
    suitable_heroes = find_suitable_heroes(emergency_ID)
    suitable_available_heroes = find_available_heroes(suitable_heroes)
    write_distances(suitable_available_heroes)
    write_rankings(emergency_ID,suitable_available_heroes)
    display_page_3(1,emergency_ID)

####################################################
################# MEETING ##########################
####################################################

def meeting():
    print('meeting')
    home_screen()

####################################################
################# MAIN FUNCTION ####################
####################################################
def home_screen():
#HOME SCREEN - START HERE
    gotoscreen1()
    while True:
        button_pressed = buttons_check()
        message_received = message_check()
        if message_received:
            if message_received in ['Y','N']:
                display_message(message_received)
            else:
                emergency(message_received)
        elif button_pressed == 2:
            meeting()

class thewindow(QtWidgets.QMainWindow):
    def timerEvent(self, event):
        esend.getMessages()
        emergency(esend.getMostRecentMessage())
        display_message(esend.getMostRecentMessage())
        print("asdf")

#switch_LEDs(1111)
import sys
import receiver

esend = receiver.SMS_Reciever("d")
esend.getMessages()
emergency(esend.getMostRecentMessage())

app = QtWidgets.QApplication(sys.argv)
MainWindow = thewindow()
ui = GUI.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.startTimer(5000)

#xui.blueButton = #SQL Query?
#ui.redButton = #
#ui.messageBox1 = #endedex message
MainWindow.show()
sys.exit(app.exec_())
