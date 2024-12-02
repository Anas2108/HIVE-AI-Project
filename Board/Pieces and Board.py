

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


    def get_free_region_of_piece(self , piece :'Piece') :
        x,y = piece.position
        list =[(x+1, y),(x+1,y-1),(x+1,y+1),(x,y-1),(x,y+1),(x-1,y)]
        returnList = []
        for i in range(6) :
          x,y = list[i] 
          if  self.board.board_2d[x][y] == 0:
              returnList.append((x,y))
              
        return returnList
        
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
                self.valid_moves = [(x+1, y),(x+1,y-1),(x+1,y+1),(x,y-1),(x,y+1),(x-1,y)]
                return self.valid_moves
            else :
               if self.type == -1 or self.type == -2:
                   self.valid_moves = self.get_valid_moves_of_block(self.board.black_piece,self.board.white_piece)
                   return self.valid_moves
               elif self.type == 1 or self.type == 2 :
                  self.valid_moves = self.get_valid_moves_of_block(self.board.white_piece,self.board.black_piece)
                  return self.valid_moves
                
                   
                   
                

       

      


def main():
    # Create a board with size 3x3
    board = Board(10)
    # board.board_2d[5][5] = -1
    # board.board_2d[6][5] = -1
    # board.board_2d[6][3] =  1
    # board.board_2d[7][4] =  1




    piece1 =Piece(-1,(-1,-1),"el sakarta7",board)
    piece2 =Piece(1,(-1,-1),"el sakarta7",board)
    piece3 =Piece(-2,(-1,-1),"el sakarta7",board)
    piece4 =Piece(2,(-1,-1),"el sakarta7",board)

    


    # board.pieces.append(piece)
    # board.black_piece.append(piece1)
    # board.black_piece.append(piece2)
    # board.white_piece.append(piece3)
    # board.white_piece.append(piece4)



    # piece5 =Piece(-1,(-1,-1),"el sakarta7",board)
    
    

    
    x = []
    x = piece1.valid_moves_func()
    print(x)

    board.place_piece(piece1,(5,5))

    

    x=piece2.valid_moves_func()
    print(x)

    board.place_piece(piece2,(6,5))
    
    x=piece3.valid_moves_func()
    print(x) 
   
    board.place_piece(piece3,(5,4))

    x=piece4.valid_moves_func()
    print(x) 

    print(board.pieces[1].position)
if __name__ == "__main__":
    main()