%dynamic rule
:-use_module(library(lists)). 
:-abolish(height/1).
:-abolish(width/1).
:-abolish(pacman/3).
:-abolish(ghost/4).
:-abolish(powerBall/2).
:-abolish(ghostPrev/3).
:-dynamic pacman/3.
:-dynamic ghost/4.
:-dynamic powerBall/2.
:-dynamic ghostPrev/3.
:-dynamic height/1.
:-dynamic width/1.


grid(
   [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
	[1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
	[1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
	[1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
	[1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1],
	[3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,3],
	[1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
	[1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
	[1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
	[1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
	[1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
	[1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
	[1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
	[1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]).

pacman(14,24,normal).
powerBall(2,4).
powerBall(27,4).
powerBall(2,14).
powerBall(27,14).
ghost(14,12,red,chase).
ghostPrev(14,13,red).
ghost(14,12,pink,scatter).
ghostPrev(14,13,pink).
ghost(14,12,blue,chase).
ghostPrev(14,13,blue).
ghost(14,12,orange,chase).
ghostPrev(14,13,orange).


%up (currentPosition, possibleMove1, possibleMove1, output).
priority((OldX,OldY),(X,Y),(W,Z),(OldX,Ny)):- Ny is OldY - 1, X == OldX, Y == Ny.
priority((OldX,OldY),(X,Y),(W,Z),(OldX,Ny)):- Ny is OldY - 1, W == OldX, Z == Ny.
%left
priority((OldX,OldY),(X,Y),(W,Z),(Nx,OldY)):- Nx is OldX - 1, X == Nx, Y == OldY.
priority((OldX,OldY),(X,Y),(W,Z),(Nx,OldY)):- Nx is OldX - 1, W == Nx, Z == OldY.
%down
priority((OldX,OldY),(X,Y),(W,Z),(OldX,Ny)):- Ny is OldY + 1, X == OldX, Y == Ny.
priority((OldX,OldY),(X,Y),(W,Z),(OldX,Ny)):- Ny is OldY + 1, W == OldX, Z == Ny.
%right
priority((OldX,OldY),(X,Y),(W,Z),(Nx,OldY)):- Nx is OldX + 1, X == Nx, Y == OldY.
priority((OldX,OldY),(X,Y),(W,Z),(Nx,OldY)):- Nx is OldX + 1, W == Nx, Z == OldY.

restart:-
  reconsult('/Users/patricksuphalawut/Documents/Project/Third_year_1s/ai/prolog-ai.pl'),
  start.

reset:-
  resetPacman,
  resetGhost.


width(28).
height(31).

%find the element in X and Y position Param(X,Y,value of element in that position)
element(X,Y,Z):-
  grid(G),
  nth1(Y,G,Line),
  nth1(X,Line,Z).

alive:-
  pacman(X,Y,beast),
  ghost(X,Y,T,scare),
  eatGhost.

alive:-
  pacman(X,Y,_),
  ghost(X,Y,T,Z),
  Z \= scare.


%pacman logic what is element on the pacman block.
validatePos(X,Y):-
    element(X,Y,1), !, fail.

validatePos(X,Y):-
  powerBall(X,Y),
  retract(powerBall(X,Y)),
  retract(pacman(Px,Py,_)),
  assert(pacman(X,Y,beast)),
  changeAllGhostsMode(scare).

validatePos(X,Y).


%wrap portal logic
wrap(X,Y,NX,NY):-
  element(X,Y,Z),
  Z > 1,
  element(NX,NY,Z),
  \+ (NX== X, NY == Y), !.
getMap(G):-
  grid(G).

getPacman(X,Y):-
  pacman(X,Y,_).

getGhost(Type,X,Y,Mode):-
  ghost(X,Y,Type,Mode).

getGhostPrev(Type,X,Y):-
  ghostPrev(X,Y,Type).

%move pacman to new position
movePacman(X,Y):-
    \+ghost(X,Y,_,scare),
    pacman(_,_,normal),
    fail.


movePacman(X,Y):-
  ghost(X,Y,T,scare),
  validatePos(X,Y),
  retract(pacman(_,_,Type)),
  assert(pacman(X,Y,Type)),
  eatGhost.

movePacman(X,Y):-
  wrap(X,Y,NX,NY),
  validatePos(NX,NY),
  retract(pacman(_,_,Type)),
  assert(pacman(NX,NY,Type)),write("aslkfjkl"),nl.

movePacman(X,Y):-
  validatePos(X,Y),
  retract(pacman(_,_,Type)),
  assert(pacman(X,Y,Type)).

changeGhostMode(Type,Mode):-
  retract(ghost(X,Y,Type,_)),
  assert(ghost(X,Y,Type,Mode)).

changeAllGhostsMode(Mode):-
  retract(ghost(X1,Y1,red,_)),
  retract(ghost(X2,Y2,blue,_)),
  retract(ghost(X3,Y3,pink,_)),
  retract(ghost(X4,Y4,orange,_)),
  assert(ghost(X1,Y1,red,Mode)),
  assert(ghost(X2,Y2,blue,Mode)),
  assert(ghost(X3,Y3,pink,Mode)),
  assert(ghost(X4,Y4,orange,Mode)).

moveRedGhost:-
  pacman(Px,Py,_),
  moveGhost(red,(Px,Py)).

moveRedGhost(X,Y):- moveGhost(red,(X,Y)).

moveBlueGhost(X,Y):-
  moveGhost(blue,(X,Y)).

movePinkGhost(X,Y):-
  moveGhost(pink,(X,Y)).

moveOrangeGhost:-
  moveGhost(orange,G).


%for chase mode
%red ghost target
moveGhost(Type,Goal):-
  Type == red,
  ghost(X,Y, red, chase),
  targetGhost((X,Y),(NewX,NewY),Goal,Type),!,
  moveGhost(NewX,NewY,red,chase).

%orange ghost
moveGhost(Type,Goal):-
  Type == orange,
  ghost(X,Y, Type, chase),
  orangeGhost((X,Y),(NewX,NewY)),!,
  moveGhost(NewX,NewY,Type,chase).

%blue and pink ghost
moveGhost(Type,Goal):-
  ghost(X,Y, Type, chase),
  targetGhost((X,Y),(NewX,NewY),Goal,Type),!,
  moveGhost(NewX,NewY,Type,chase).

%for scatter mode
moveGhost(Type,Goal):-
  ghost(X,Y,Type,scatter),write("hey"),
  scatterGhost((X,Y),(NX,NY),Type),!,
  moveGhost(NX,NY,Type,scatter).

%for scare mode when pacman eat power ball
moveGhost(Type,Goal):-
  ghost(X,Y,Type,scare),write("HI"),
  scatterGhost((X,Y),(NX,NY),Type),!,
  moveGhost(NX,NY,Type,scare).

%move ghost to new position
moveGhost(X,Y,Type,Mode):-
  wrap(X,Y,NX,NY),
    retract(ghost(W,Z,Type,Mode)),
    retract(ghostPrev(_,_,Type)),
    assert(ghost(NX,NY,Type,Mode)),
    assert(ghostPrev(W,Z,Type)),!,
  \+alive.

moveGhost(X,Y,Type,Mode):-
  retract(ghost(W,Z,Type,Mode)),
  retract(ghostPrev(_,_,Type)),
  write(X), write("/"),write(Y),nl,
  assert(ghost(X,Y,Type,Mode)),
  assert(ghostPrev(W,Z,Type)),!,
  \+alive.


%ghost target X point. param(currentPosition,nextposition,goalposition,typeofghost).
targetGhost(CurrPoint,(NextX,NextY),Goal,Type):-
  ghostPrev(Xprev,Yprev,Type),
  write("Goal: "),write(Goal),nl,
  astar(CurrPoint,[],Goal,[(Xprev,Yprev),(14,13),(15,13)],[(X1,Y1),(NextX,NextY)|T],1,Temp,TotalCost).
  %%turnBase(CurrPoint,Goal,Type,(NextX,NextY)).

%orange ghost behaviour param(CurrentPosition,outputPosition).
orangeGhost(CurrPoint,NextMove):-
  pacman(Px,Py,_),
  h(CurrPoint,(Px,Py),D),
  D < 8,
  scatterGhost(CurrPoint,NextMove,orange).

orangeGhost(CurrPoint,NextMove):-
  pacman(Px,Py,_),
  h(CurrPoint,(Px,Py),D),
  D >= 8,
  targetGhost(CurrPoint,NextMove,(Px,Py),orange).

%scatter mode for each type of ghost param(currentPosition,outputPosition,Typeofghost)
scatterGhost(CurrPoint,NextMove,Type):-
  Type == red,
  turnBase(CurrPoint,(27,1),Type,NextMove).

scatterGhost(CurrPoint,NextMove,Type):-
  Type == blue,
  turnBase(CurrPoint,(2,1),Type,NextMove).

scatterGhost(CurrPoint,NextMove,Type):-
  Type == pink,
  turnBase(CurrPoint,(27,31),Type,NextMove).

scatterGhost(CurrPoint,NextMove,Type):-
  Type == orange,
  turnBase(CurrPoint,(2,31),Type,NextMove).


% get every adjust block that is not a wall param(startPoint, visitedPoint,output).
findAdj(StartPoint,[],PossibleMove):-
  findall((X,Y),(adj(StartPoint,(X,Y)), \+element(X,Y,1)), PossibleMove).

% get every adjust block that is not a wall and not already visit.
findAdj(StartPoint,Visited,PossibleMove):-
  findall((X,Y),(adj(StartPoint,(X,Y)), \+element(X,Y,1), \+member((X,Y),Visited)), PossibleMove).

adj((X,Y),(X,NY)) :-
  height(H),
  Y < H,
  NY is Y + 1.

adj((X,Y),(X,NY)) :-
    Y > 1,
    NY is Y - 1.

adj((X,Y),(NX,Y)) :-
    width(W),
    X < W,
    NX is X + 1.

adj((X,Y),(NX,Y)) :-
    X > 1,
    NX is X - 1.

adj((X,Y),(NX,NY)):- wrap(X,Y,NX,NY), write("heyyy").

%find distance param(Point1,Point2, output)
h((X,Y),(X2,Y2),D) :-
    D is sqrt(((X - X2)**2) + ((Y - Y2)**2)).

%param(Element you want to del,array,output)
removeElement(N,[],[]):- !.
removeElement(N,[H|T],Z):- N == H, removeElement(N,T,Z).
removeElement(N,[H|T],[H|Z]):- removeElement(N,T,Z).

% a star param(currentPosition,openlist,GoalPosition,VisitedPoint, outputPath, totalG, temp,outputCost)
astar((X,Y),Open,(X,Y),Visited,[(X,Y)],GValue,Temp,Temp):- !.
astar((X,Y),Open,Goal,Visited,[(X,Y)|T],GValue,Temp,Temp):- GValue >= 5,!.
astar((X,Y),[],Goal,Visited,[(X,Y)|T],GValue,Temp,TotalCost):-
  findAdj((X,Y),Visited,PossiblePoint),
  %%write("P: "),write(PossiblePoint),nl,
  %% get_from_heap(Heap,Key,NexT,NewHeap),
  %% append(PossiblePoint,Open,NewPossible),
  recur(PossiblePoint,Goal,H,NextPoint),
  removeElement(NextPoint,PossiblePoint,NV),
  append([(X,Y)|Visited],NV,NewVisit),
  %%write("N: "),write(NextPoint),nl,
  %%write("V: "),write(NewVisit),nl,write("cost: "),write(GValue),nl,
  TotalCost1 is GValue + H,
  NewG is GValue + 1,
  astar(NextPoint,[],Goal,NewVisit,T,NewG,TotalCost1,TotalCost).

astar((X,Y),(W,Z),Goal,Visited,[(X,Y)|T],GValue,Temp,TotalCost):-
  findAdj((X,Y),Visited,PossiblePoint),
  %% write("P: "),write(PossiblePoint),nl,
  %% get_from_heap(Heap,Key,NexT,NewHeap),
  %% append(PossiblePoint,Open,NewPossible),
  recur(PossiblePoint,Goal,H,NextPoint),
  removeElement(NextPoint,PossiblePoint,NV),
  append([(X,Y)|Visited],NV,NewVisit),
  %%write("N1: "), write(NextPoint),nl,
  %% write("N: "),write(NextPoint),nl,write("V: "),write(NewVisit),nl,write("cost: "),write(GValue),nl,
  TotalCost1 is GValue + H,
  %% write("w: "), write(W),write("Z: "), write(Z),nl,
  h((W,Z),Goal,H1),
  %% write("T: "), write(TotalCost1),nl,
  %% write("H1: "), write(h1),nl,
  TotalCost1 < H1,
  NewG is GValue + 1,

  astar(NextPoint,(W,Z),Goal,NewVisit,T,NewG,TotalCost1,TotalCost).

%% astar((X,Y),(W,Z),Goal,Visited,[(X,Y)|T],GValue,Temp,TotalCost):-
%%   astar((W,Z),[],Goal,NewVisit,T,NewG,Temp,Temp).

%a star, but for the case that two blocks have the same cost value. param(2possibleMove,openlist,GoalPosition,VisitedPoint, outputPath, totalG, temp,outputCost)
astar([First,Second|Tail],Open,Goal,Visited,[First|Path1],GValue1,Temp,TotalCost1):-
  %% write("in 2   first:"),write(First),write("   second:  "),write(Second),nl,
  %% append([Second],Open,NewOpen),
  %% write(NewOpen),nl,
  astar(First,Second,Goal,Visited,Path1,GValue1,Temp,TotalCost1).

astar([First,Second|Tail],Open,Goal,Visited,[Second|Path1],GValue1,Temp,TotalCost1):-
  %% write("in 2   first:"),write(First),write("   second:  "),write(Second),nl,
  %% write(NewOpen),nl,
  astar(Second,[],Goal,Visited,Path1,GValue1,Temp,TotalCost1).


%compare h value param(possibleMove,GoalPosition,outputCost, outputPoint).
recur([P],Goal,H,P):- h(P,Goal,H).
recur([F|T],Goal,H,P):- recur(T,Goal,H,P), h(F,Goal,NewH), H < NewH.
recur([F|T],Goal,NewH,F):- recur(T,Goal,H,P), h(F,Goal,NewH), H > NewH.
recur([F|T],Goal,H,Z):- recur(T,Goal,H,P), h(F,Goal,NewH), H == NewH, append([F],[P],Z).

%calculate one step ahead take param(currentPosition,GoalPosition,Type of the ghost, Output).
turnBase((X,Y),Goal,Type,NextMove):-
  %% write("target: "), write(Goal),nl,
  %% write("current: "), write((X,Y)),nl,
  ghostPrev(PrevX,PrevY,Type),
  %% write("hyy"),nl,
  findAdj((X,Y),[(PrevX,PrevY),(14,13),(15,13)],AdjPoint),
  %% write("AdjPoint: "), write(AdjPoint),nl,
  %% write("hyyyy"),nl,
  recur(AdjPoint,Goal,H,NewPoint),
  turnBaseHelp(NewPoint,(X,Y),NextMove).


%for case that 2 ways have equal distance param(2PossibleMove, currentPoint, output).
turnBaseHelp((X,Y),OldPoint,(X,Y)):- !.
turnBaseHelp([First,Second|T],OldPoint,NewPoint):-
  %%write(First),nl,write(Second),nl,
  priority(OldPoint,First,Second,NewPoint),!.
  %%write("new point:"),write(NewPoint),nl.

eatGhost:-
  pacman(X,Y,_),
  retract(ghost(X,Y,T,scare)),
  assert(ghost(24,12,T,chase)),
  retract(ghostPrev(_,_,T)),
  assert(ghostPrev(24,13,T)),
  fail.
eatGhost.

resetGhost:-
  retract(ghost(X,Y,T,_)),
  assert(ghost(24,12,T,scatter)),
  retract(ghostPrev(_,_,T)),
  assert(ghostPrev(24,13,T)),
  fail.
resetGhost.


resetPacman:-
  retract(pacman(_,_,_)),
  assert(pacman(4,24,normal)).

hh(Z):- Z is sqrt(2).
%% hh:-
%%  dappend([1,2,3 | Tail1]-Tail1, [4,5,6| Tail2]-Tail2, Result-Tail3),
%%  write(Result-[]).
%%  %% dappend([Result|Tail3]-Tail3, [4,5,6| Tail4]-Tail4, Result1-[]),
%%  %% write(Result1),

%% dappend(List1-Tail1, Tail1-Tail2, List1-Tail2).

%% as_difflist([], Back-Back).
%% as_difflist([Head| Tail], [Head| Tail2]-Back) :-
%%     as_difflist(Tail, Tail2-Back).

