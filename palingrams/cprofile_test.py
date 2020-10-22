"""
Profiling find_palingrams with cProfile 
"""
import  cProfile
import palingrams

cProfile.run(palingrams.find_palingrams())