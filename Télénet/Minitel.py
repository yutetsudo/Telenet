#!/bin/python3
# -*- coding: utf-8 -*-
import Télénet.TermConst as TermConst
import os


class Minitel:
    def __init__(self, reader, writer) -> None:
        self.reader = reader
        self.writer = writer

    # region Output
    def print(self, text):
        """Print text to minitel

        Parameters
        ----------
        text : str
            String to print

        See Also
        --------
        self.convertToMinitel() :
            Convert minitel unicode to ascii unicode
        """
        self.writer.write(self.convertToMinitel(text))

    def sendData(self, data):
        """Send raw data to minitel

        Parameters
        ----------
        data : str
            Data to send to minitel
        """
        self.writer.write(data)

    def printStatus(self, text):
        """Print text on the status bar of minitel

        Parameters
        ----------
        text : str
            Text to print on status bar
        """
        self.clearStatus()
        if len(text) < 38:
            self.setPos(0, 0)
            self.print(self.convertToMinitel(text))

    def beep(self):
        """Send a simple beep on minitel
        """
        self.sendData(TermConst.BELL)

    def read(self, file):
        """Read Videotext file and send it to minitel

        Parameters
        ----------
        file : str
            *.VDT file location
        """
        with open(file, 'r') as VDT:
            self.sendData(VDT.read())

    def convertToMinitel(self, text):
        """Convert minitel unicode to ascii unicode

        Parameters
        ----------
        text : str
            Minitel text that need to be converted

        Returns
        -------
        str
            Converted text
        """
        text = text.replace('£', ''.join([TermConst.SS2, chr(0x23)]))
        text = text.replace('°', ''.join([TermConst.SS2, chr(0x30)]))
        text = text.replace('à', ''.join([TermConst.SS2, chr(0x41), chr(0x61)]))
        text = text.replace('â', ''.join([TermConst.SS2, chr(0x43), chr(0x61)]))
        text = text.replace('ä', ''.join([TermConst.SS2, chr(0x48), chr(0x61)]))
        text = text.replace('è', ''.join([TermConst.SS2, chr(0x41), chr(0x65)]))
        text = text.replace('é', ''.join([TermConst.SS2, chr(0x42), chr(0x65)]))
        text = text.replace('ê', ''.join([TermConst.SS2, chr(0x43), chr(0x65)]))
        text = text.replace('ë', ''.join([TermConst.SS2, chr(0x48), chr(0x65)]))
        text = text.replace('î', ''.join([TermConst.SS2, chr(0x43), chr(0x69)]))
        text = text.replace('ï', ''.join([TermConst.SS2, chr(0x48), chr(0x69)]))
        text = text.replace('ô', ''.join([TermConst.SS2, chr(0x43), chr(0x6F)]))
        text = text.replace('ö', ''.join([TermConst.SS2, chr(0x48), chr(0x6F)]))
        text = text.replace('ù', ''.join([TermConst.SS2, chr(0x41), chr(0x75)]))
        text = text.replace('û', ''.join([TermConst.SS2, chr(0x43), chr(0x75)]))
        text = text.replace('ü', ''.join([TermConst.SS2, chr(0x48), chr(0x75)]))
        text = text.replace('ç', ''.join([TermConst.SS2, chr(0x4B), chr(0x63)]))
        text = text.replace('←', ''.join([TermConst.SS2, chr(0x2C)]))
        text = text.replace('↑', ''.join([TermConst.SS2, chr(0x2D)]))
        text = text.replace('→', ''.join([TermConst.SS2, chr(0x2E)]))
        text = text.replace('↓', ''.join([TermConst.SS2, chr(0x2F)]))
        text = text.replace('¼', ''.join([TermConst.SS2, chr(0x3C)]))
        text = text.replace('½', ''.join([TermConst.SS2, chr(0x3D)]))
        text = text.replace('¡', ''.join([TermConst.SS2, chr(0x3E)]))
        text = text.replace("—", ''.join([chr(0x60)]))
        text = text.replace('|', ''.join([chr(0x7C)]))
        return text
    # endregion


    # region Move
    def setPos(self, x, y):
        """Set cursor absolute position

        Parameters
        ----------
        x : int
            horizontal row axis 
        y : int
            vertical column axis
        """
        self.writer.write(TermConst.UNIT_SEPARATOR)
        self.writer.write(chr(0x40+y))
        self.writer.write(chr(0x41+x))
    # endregion


    # region Clear
    def clear(self):
        """Clear minitel screen except status bar
        """
        self.writer.write(TermConst.NEW_PAGE)

    def clearLine(self, line):
        """Clear the whole line

        Parameters
        ----------
        line : int
            Set the line to clear
        """
        self.setPos(0, line)
        self.writer.write(TermConst.CLEAR_EOL)

    def clearStatus(self):
        """Clear the status bar
        """
        self.setPos(0, 0)
        self.writer.write(TermConst.CLEAR_EOL)

    def clearAll(self):
        """Clear everything
        """
        self.clear()
        self.clearStatus()
    # endregion


    # region Effect
    def normal(self):
        self.setColor(fg='WHITE', bg='BLACK')
        self.setSize('NORMAL')
        self.writer.write(TermConst.NORMAL_SIZE)
        self.writer.write(TermConst.NORMAL_VIDEO)

    def setSize(self, size=None):
        """Set the text size

        Parameters
        ----------
        size : str
            [NORMAL, DOUBLE_HEIGHT, DOUBLE_WIDTH, DOUBLE]\n
            Set the size, by default None
        """
        if size != None:
            self.sendData(
                ''.join([TermConst.ESCAPE, chr(0x4C + TermConst.SIZE[size])]))

    # def blink(self, state = None):
    #    if state != None:
    #        self.sendData(''.join([TermConst.ESCAPE, TermConst.BLINK[state]]))

    # def underline(self, state = None):
    #    if state != None:
    #        self.sendData(''.join([TermConst.ESCAPE, TermConst.UNDERLINE[state]]))

    # def invert(self, state = None):
    #    if state != None:
    #        self.sendData(''.join([TermConst.ESCAPE, TermConst.BLINK[state]]))

    def cursor(self, state=None):
        """Set the cursor ON or OFF

        Parameters
        ----------
        state : str
            [ON, OFF]\n
            Set the cursor state, by default None
        """
        if state != None:
            self.writer.write(TermConst.CURSOR[state])

    def setColor(self, fg=None, bg=None):
        """Set the text color

        Parameters
        ----------
        fg : str, optional
            [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]\n
            Set the foreground color, by default None

        bg : str, optional
            [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]\n
            Set the background color, by default None
        """
        if fg != None:
            self.sendData(
                ''.join([TermConst.ESCAPE, chr(0x40 + TermConst.COLOR[fg])]))
        if bg != None:
            self.sendData(
                ''.join([TermConst.ESCAPE, chr(0x50 + TermConst.COLOR[bg])]))
    # endregion


    # region Input
    def reciveData(self):
        """Recive data from Minitel

        Returns
        -------
        str
            Return the Minitel data
        """
        key = self.reader.read(1)
        return key

    def toMinitelKey(self, key):
        """Convert Minitel key to text

        Parameters
        ----------
        key : str
            Key sended by the minitel

        Returns
        -------
        str
            Corresponding key
        """
        functionKey = ""
        if key == TermConst.ENVOI:
            functionKey = "ENVOI"
        elif key == TermConst.RETOUR:
            functionKey = "RETOUR"
        elif key == TermConst.REPETITION:
            functionKey = "REPETITION"
        elif key == TermConst.GUIDE:
            functionKey = "GUIDE"
        elif key == TermConst.ANNULATION:
            functionKey = "ANNULATION"
        elif key == TermConst.SOMMAIRE:
            functionKey = "SOMMAIRE"
        elif key == TermConst.CORRECTION:
            functionKey = "CORRECTION"
        elif key == TermConst.SUITE:
            functionKey = "SUITE"
        elif key == TermConst.CONNEXION:
            functionKey = "CONNEXION"
        else:
            functionKey = "NULL"
        return functionKey

    async def getKey(self):
        """Get key from minitel

        Returns
        -------
        str
            return key
        """
        key = await self.reciveData()
        if key != "":
            if key == TermConst.DEVICE_CONTROL_3:
                key = await self.reciveData()
                key = self.toMinitelKey(key)
            return key

    async def textInput(self, x, y, fg='WHITE', bg='BLACK', size='NORMAL',
                        EOFKey="ENVOI", replaceBy=".", maxSize=40, passwordField=False):
        """[summary]

        Parameters
        ----------
        x : int
            horizontal row axis 
        y : int
            vertical column axis
        fg : str, optional
            [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]\n
            Set the foreground color, by default 'WHITE'
        bg : str, optional
            [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]\n
            Set the background color, by default 'BLACK'
        size : str, optional
            [NORMAL, DOUBLE_HEIGHT, DOUBLE_WIDTH, DOUBLE]\n
            Set the size, by default 'NORMAL'
        EOFKey : str, optional
            End of file Key, by default "ENVOI"
        replaceBy : str, optional
            Character to replace by, by default "."
        maxSize : int, optional
            Maximum field size, by default 40
        passwordField : bool, optional
            Change echo to '*', by default False

        Returns
        -------
        str
            output variable
        """
        loop = True
        string = []
        self.setPos(x, y)
        self.setColor(fg, bg)
        self.setSize(size)
        self.cursor('ON')

        while loop:
            key = await self.getKey()
            if key == EOFKey:
                loop = False
            elif key == "CORRECTION":
                if len(string) != 0:
                    self.writer.write(TermConst.CURSOR_LEFT)
                    self.print(replaceBy)
                    self.writer.write(TermConst.CURSOR_LEFT)
                    string.pop()
            else:
                if len(string) < maxSize:
                    self.print('*' if passwordField else key)
                    string.append(key)
                else:
                    self.printStatus("Text trop long")
                    if x + len(string) < 40:
                        self.setPos(x + len(string), y)
                    else:
                        self.setPos((x + len(string)) - 40, y+1)
        self.cursor('OFF')
        return ''.join(string)
    # endregion


    # region Misc
    def init(self):
        os.system('cls' if os.name in ('nt', 'dos')
                  else 'clear')
        self.clearAll()
        self.cursor('OFF')
        self.setPos(0, 1)

    def hang(self):
        self.writer.write(chr(0x1b))
        self.writer.write(chr(0x39))
        self.writer.write(chr(0x67))
    # endregion
