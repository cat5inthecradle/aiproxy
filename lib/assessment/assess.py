# Normal imports
import csv, glob, json, time, os
from multiprocessing import Pool
import concurrent.futures
import io
import json
import logging

# Import our support classes
from lib.assessment.config import SUPPORTED_MODELS, VALID_GRADES
from lib.assessment.grade import Grade
from lib.assessment.report import Report
from lib.assessment.rubric_tester import (
    read_inputs,
    get_expected_grades,
    get_examples,
    get_passing_grades,
    get_student_files,
    validate_rubrics,
    validate_students,
    grade_student_work,
    compute_accuracy
)

def grade(code, prompt, rubric, examples=[], api_key='', llm_model='gpt-4', num_responses=1, temperature=0.2, num_passing_grades=2, remove_comments=False):
  OPENAI_API_KEY = api_key

  # Set the key
  if OPENAI_API_KEY:
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  elif not 'OPENAI_API_KEY' in os.environ:
    logging.error("Must set OPENAI_API_KEY!")
    return {}
  else:
    logging.info("Using set OPENAI_API_KEY")

  grade = Grade()
  return grade.grade_student_work(
      prompt, rubric, code, "student",
      examples=examples,
      use_cached=False,
      write_cached=False,
      num_responses=num_responses,
      temperature=temperature,
      llm_model=llm_model,
      remove_comments=remove_comments
  )
