from enum import Enum

class HexMoveCaseEvenEven(Enum):
    TOP = (-1, 0)
    DOWN = (1, 0)
    TOP_RIGHT = (-1, 1)
    TOP_LEFT = (-1, -1)
    LOWER_LEFT = (0, -1)
    LOWER_RIGHT = (0, 1)


class HexMoveCaseOddOdd(Enum):
    TOP = (-1, 0)
    DOWN = (1, 0)
    TOP_RIGHT = (0, 1)
    TOP_LEFT = (0, -1)
    LOWER_LEFT = (1, -1)
    LOWER_RIGHT = (1, 1)
class Board:
    def __init__(self, size: int):
        # Initialize a 2D list with zero
        self.board_2d = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.pieces = []      # list to store Piece objects
        self.black_piece = [] # list of black pieces
        self.white_piece = [] # list of white pieces
    def check_empty_board(self) -> bool:       
        return all(all(element == 0 for element in row) for row in self.board_2d)
    
    def place_piece (self, piece : 'Piece' ,position : tuple[int,int] ):
        self.pieces.append(piece)
        if piece.type == -1 or piece.type == -2:
          self.black_piece.append(piece)

        elif piece.type == 1 or piece.type == 2:
          self.white_piece.append(piece)
        x,y = position
        self.board_2d[x][y] = piece.type
        piece.position = position


class Piece:
    def __init__(self, type: int, position: tuple[int, int], insect_type: str, board: Board):
        """
        type
        -1 ---->black
        -2 -----> Queen Bee Black
         1 ----->white
         2 ---->Queen Bee White

        position 
        -1,-1 --> outside the board
        """
        self.type = type
        self.position = position
        self.insect_type = insect_type
        self.board = board
        self.valid_moves = None  # or [] depending on the expected usage


    def check_coordinates(self , x:int, y:int):
    # Check if (x is even and y is even) or (x is odd and y is even)
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 == 0):
            return [(x-1,y),(x-1,y+1),(x,y+1),(x+1,y),(x , y-1),(x-1,y-1)]
        else:
            return [(x+1,y),(x+1,y-1),(x+1,y+1),(x,y-1),(x,y+1),(x-1,y)]
            
    def get_free_region_of_piece(self , piece :'Piece') :
        x,y = piece.position
        list =piece.check_coordinates(x,y)
        returnList = []
        for i in range(6) :
          x,y = list[i] 
          if  self.board.board_2d[x][y] == 0:
              returnList.append((x,y))
              
        return returnList
        
    def get_occupied_region_of_piece(self , piece :'Piece') :
        x,y = piece.position
        list =piece.check_coordinates(x,y)
        returnList = []
        for i in range(6) :
          x,y = list[i] 
          if  self.board.board_2d[x][y] != 0:
              returnList.append((x,y))
              
        return returnList

    def hopper_get_valid_pos_of_direction(self, direction :tuple[int,int], piece_position:tuple[int,int]):
        x,y = piece_position
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 == 0):
            if direction == HexMoveCaseEvenEven.TOP.value :
                x,y = piece_position
                while (self.board.board_2d[x][y] !=0):
                    x = x-1

                return (x,y)

            elif direction == HexMoveCaseEvenEven.DOWN.value :
                x,y = piece_position
                while (self.board.board_2d[x][y] !=0):
                    x = x+1

                return (x,y)

            elif direction == HexMoveCaseEvenEven.TOP_LEFT.value :
                counter = 0
                x,y = piece_position 
          
                while(self.board.board_2d[x][y] !=0):
                    y = y-1
                    if counter %2 == 0 :
                        x =x-1
                    counter = counter + 1

                return (x,y)

            elif direction == HexMoveCaseEvenEven.TOP_RIGHT.value:
                counter = 0
                x,y = piece_position 
        
                while(self.board.board_2d[x][y] !=0):
                    y = y+1
                    if counter %2 == 0 :
                        x =x-1
                    counter = counter + 1

                return (x,y)     

            elif direction == HexMoveCaseEvenEven.LOWER_LEFT.value :
                counter = 0
                x,y = piece_position 
                
                while(self.board.board_2d[x][y] !=0):
                    y = y-1
                    if counter %2 != 0 :
                        x =x+1
                    counter = counter + 1

                return (x,y)    

                               

            elif direction == HexMoveCaseEvenEven.LOWER_RIGHT.value :
                counter = 0
                x,y = piece_position 
              
                while(self.board.board_2d[x][y] !=0):
                    y = y+1
                    if counter %2 != 0 :
                        x =x+1
                    counter = counter + 1

                return (x,y)    

                    

                   

        else:
            if direction == HexMoveCaseOddOdd.TOP.value :
                x,y = piece_position
                while (self.board.board_2d[x][y] !=0):
                    x = x-1

                return (x,y)

            elif direction == HexMoveCaseOddOdd.DOWN.value :
                x,y = piece_position
                while (self.board.board_2d[x][y] !=0):
                    x = x+1

                return (x,y)

            elif direction == HexMoveCaseOddOdd.TOP_LEFT.value :
                counter = 0
                x,y = piece_position 
                
                while(self.board.board_2d[x][y] !=0):
                    y = y-1
                    if counter %2 != 0 :
                        x =x-1
                    counter = counter + 1

                return (x,y)         

            elif direction == HexMoveCaseOddOdd.TOP_RIGHT.value:
                counter = 0
                x,y = piece_position 
                
                while(self.board.board_2d[x][y] !=0):
                    y = y+1
                    if counter %2 != 0 :
                        x =x-1
                    counter = counter + 1

                return (x,y)    

                    

                

            elif direction == HexMoveCaseOddOdd.LOWER_LEFT.value :
                counter = 0
                x,y = piece_position 
           

                
                while(self.board.board_2d[x][y] !=0):
                    y = y-1
                    if counter %2 == 0 :
                        x =x+1
                    counter = counter + 1

                return (x,y)                   

            elif direction == HexMoveCaseOddOdd.LOWER_RIGHT.value :
                counter = 0
                x,y = piece_position 
   
             
                while(self.board.board_2d[x][y] !=0):
                    y = y+1
                    if counter %2 == 0 :
                        x =x+1
                    counter = counter + 1

                return (x,y)  

    def hopper_valid_moves(self):
        
        list = self.get_occupied_region_of_piece(self) 
        list_valid = []
        x1,y1 =self.position
        for i in range (len(list)):
            x2,y2 = list[i]
            x2 = x2-x1
            y2 = y2-y1
            list_valid.append(self.hopper_get_valid_pos_of_direction((x2,y2),self.position))
         #The call of One Hive Rule
        return list_valid
    
    def beetle_valid_moves(self):
        x,y = self.position

        list_valid = self.check_coordinates(x,y)
        #The call of One Hive Rule
        return list_valid
    
    def get_valid_moves_of_block(self , myTurn : list['Piece'],opponent : list['Piece']) :
        available_list =[]
        excluded_list = []
        for i in range(len(myTurn)):
            available_list.extend(self.get_free_region_of_piece(myTurn[i]))
        available_list = set(available_list)
        
        for i in range(len(opponent)):
          excluded_list.extend(self.get_free_region_of_piece(opponent[i]))
        excluded_list =  set(excluded_list)
        
        

        return  list(available_list - excluded_list)
        
        
        

    def valid_moves_func(self) :
        """
        Determines the valid moves for the piece based on its position and board state.

        Returns:
            list[tuple[int, int]]: A list of valid moves as tuples of (row, column).
        """
        if self.position == (-1, -1):  # The piece is outside the board (not used yet)
            if self.board.check_empty_board():  # If the board is empty
                self.valid_moves = [(int(self.board.size/2), int(self.board.size/2))]
                return  self.valid_moves # Place the piece at the center of the board
            elif len(self.board.pieces) ==1 :
                old_piece =self.board.pieces[0].position
                x, y = old_piece  # Unpack the tuple
                self.valid_moves = self.check_coordinates(x,y)
                return self.valid_moves
            else :
               if self.type == -1 or self.type == -2:
                   self.valid_moves = self.get_valid_moves_of_block(self.board.black_piece,self.board.white_piece)
                   return self.valid_moves
               elif self.type == 1 or self.type == 2 :
                  self.valid_moves = self.get_valid_moves_of_block(self.board.white_piece,self.board.black_piece)
                  return self.valid_moves
                
        else:
            if self.insect_type == "hopper":
                return self.hopper_valid_moves()           
            elif self.insect_type == "beetle":
                return self.beetle_valid_moves()       
                

       

      


def main():
    # Create a board with size 3x3
    board = Board(10)
    # board.board_2d[5][5] = -1
    # board.board_2d[6][5] = -1
    # board.board_2d[6][3] =  1
    # board.board_2d[7][4] =  1




    piece1 =Piece(-1,(-1,-1),"beetle",board)
    piece2 =Piece(1,(-1,-1),"beetle",board)
    piece3 =Piece(1,(-1,-1),"hopper",board)
    piece4 =Piece(1,(-1,-1),"hopper",board)
    piece5 =Piece(1,(-1,-1),"hopper",board)
    piece6 =Piece(1,(-1,-1),"hopper",board)
    piece7 =Piece(1,(-1,-1),"hopper",board)
    piece8 =Piece(1,(-1,-1),"hopper",board)
    piece9 =Piece(1,(-1,-1),"hopper",board)
    piece10 =Piece(1,(-1,-1),"hopper",board)
    piece11 =Piece(1,(-1,-1),"hopper",board)



    



    
    
# test of the add piece
    # board.place_piece(piece1,(5,5))

    # board.place_piece(piece2,(6,6))
    
    # x = []
    # x = piece3.valid_moves_func()
   
    # print(x)

    
    board.place_piece(piece1,(5,3))

    board.place_piece(piece2,(6,4))
    
    board.place_piece(piece3,(5,2))
    board.place_piece(piece4,(4,3))
    board.place_piece(piece5,(5,4))
    board.place_piece(piece6,(5,5))
    board.place_piece(piece7,(6,5))
    board.place_piece(piece8,(7,4))
    # board.place_piece(piece9,(4,2))
    # board.place_piece(piece10,(3,2))
    # board.place_piece(piece11,(2,3))








    print( piece2.valid_moves_func()) 



    # board.place_piece(piece3,(2,2))

    # print(piece1.hopper_get_valid_pos_of_direction((0,-1),piece1.position))

if __name__ == "__main__":
    main()