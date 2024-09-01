from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Voters:
    liVoters: List[str] = field(default_factory=list)

    def add_voter(self, sVoterName) -> None:
        if sVoterName in self.liVoters:
            print(f"    {sVoterName} has already been added.")
            return
        
        self.liVoters.append(sVoterName)
        print(f"    {sVoterName} has been added.")

    def show_voters(self):
        if len(self.liVoters) == 0:
            print("There are no voters yet.")
            return
        
        for sVoterName in self.liVoters:
            print(sVoterName)


@dataclass
class Candidates:
    liCandidates: List[str] = field(default_factory=list)
    dCandidatesVotes: Dict[str, int] = field(default_factory=dict)

    def add_candidate(self, sCandidateName) -> None:
        if sCandidateName in self.liCandidates:
            print(f"    {sCandidateName} has already been added.")
            return
        
        self.liCandidates.append(sCandidateName)
        self.dCandidatesVotes[sCandidateName] = 0
        print(f"    {sCandidateName} has been added.")

    def show_candidates(self):
        if len(self.liCandidates) == 0:
            print("There are no candidates yet.")
            return

        for sCandidateName in self.liCandidates:
            print(sCandidateName)

    def show_vote_count(self):
        dSortedCandidates = dict(sorted(self.dCandidatesVotes.items(), key=lambda item: item[1], reverse=True))
        for sCandidateName, iNumVotes in dSortedCandidates.items():
            print(f"{sCandidateName}: {iNumVotes}")
        
        sWinnerCandidateName, iWinnerCandidateVotes = next(iter(dSortedCandidates.items()))

        return sWinnerCandidateName, iWinnerCandidateVotes


    def print_final_vote_counts(self):
        sWinnerCandidateName, iWinnerCandidateVotes = self.show_vote_count()
        print()
        print(f"{sWinnerCandidateName} has won with {iWinnerCandidateVotes} vote(s)!")

@dataclass
class Vote:
    voters = Voters()
    candidates = Candidates()
    dVoted = {}


    def vote(self, sVoterName, sCandidateName):
        if sVoterName not in self.voters.liVoters:
            print(f"    {sVoterName} is not in the list of voters.")
            return
        elif sVoterName in self.dVoted:
            print(f"    {sVoterName} has already voted.")
            return
            
        if sCandidateName not in self.candidates.liCandidates:
            print(f"    {sCandidateName} is not in the list of candidates.")
            return

        self.dVoted[sVoterName] = sCandidateName
        self.candidates.dCandidatesVotes[sCandidateName] += 1

        print(f"{sVoterName} has voted for {sCandidateName}.")

    def show_num_votes(self):
        print(f"{len(self.dVoted)} voters have already voted")

if __name__ == "__main__":
    vote = Vote()

    print('''                                                
        Commands:\n
            Add Candidate: '1' or 'ac':\n
                USAGE: 1 (Candidate Name)\n
            Add Voter: '2' or 'av':\n
                USAGE: 2 (Voter Name)\n
            Add Vote: '3' or 'v':\n
                USAGE: 3 (Voter Name) (Candidate Name)\n
            Show Candidates: '4' or 'sc':\n
                USAGE: 4\n
            Show Voters: 5 or 'sv':\n
                USAGE: 5\n
            Show Voting Count: '6' or 's':\n
                USGAE: 6
            End Voting: '7' or 'e'\n
                USAGE: 7
    ''')

    i = ""
    while i not in ['7', 'e']:
        i = input()
        inputs = i.split(' ')

        if inputs[0] in ['1', 'ac']:
            if len(inputs) > 2:
                print("Invalid input. USAGE: 1 (Candidate Name)")
            
            sCandidateName = inputs[1]
            vote.candidates.add_candidate(sCandidateName)

        elif inputs[0] in ['2', 'av']:
            if len(inputs) > 2:
                print("Invalid input. USAGE: 2 (Voter Name)")
            
            sVoterName = inputs[1]
            vote.voters.add_voter(sVoterName)

        elif inputs[0] in ['3', 'v']:
            if len(inputs) > 3:
                print("Invalid input. USAGE: 3 (Voter Name) (Candidate Name)")
            sVoterName = inputs[1]
            sCandidateName = inputs[2]
            vote.vote(sVoterName, sCandidateName)

        elif inputs[0] in ['4', 'sc']:
            if len(inputs) > 1:
                print("Invalid input. USAGE: 4")
            vote.candidates.show_candidates()

        elif inputs[0] in ['5', 'sv']:
            if len(inputs) > 1:
                print("Invalid input. USAGE: 5")
            vote.voters.show_voters()
        
        elif inputs[0] in ['6', 's']:
            if len(inputs) > 1:
                print("Invalid input. USAGE: 6")
            vote.show_num_votes()

        elif inputs[0] in ['7', 'e']:
            if len(inputs) > 1:
                print("Invalid input. USAGE: 7") 

            break

        else:
            print("Wrong input.")            
            print('''                                                
                Commands:\n
                    Add Candidate: '1' or 'ac':\n
                        USAGE: 1 (Candidate Name)\n
                    Add Voter: '2' or 'av':\n
                        USAGE: 2 (Voter Name)\n
                    Add Vote: '3' or 'v':\n
                        USAGE: 3 (Voter Name) (Candidate Name)\n
                    Show Candidates: '4' or 'sc':\n
                        USAGE: 4\n
                    Show Voters: 5 or 'sv':\n
                        USAGE: 5\n
                    Show Voting Count: '6' or 's':\n
                        USGAE: 6
                    End Voting: '7' or 'e'\n
                        USAGE: 7
            ''')
        
        print()

    vote.candidates.print_final_vote_counts()
