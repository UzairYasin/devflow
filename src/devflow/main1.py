#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from devflow.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):

    @start()
    def write_code(self):
        print("Writing Code")
        result = (
            DevCrew().crew()
            .kickoff(inputs = {"problem": "Write a code in python to print fibbonacci series."})
        )
        
    @listen(write_code)
    def review_code(self):
        print("Optimizing code :")
        result = (
            DevCrew().review_code()
        )
        
        print(result)


def kickoff():
    dev_flow = DevFlow()
    dev_flow.kickoff()

def plot():
    dev_flow = DevFlow()
    dev_flow.plot()

if __name__ == "__main__":
    kickoff()
