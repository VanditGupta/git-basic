{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_ran=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for ix in range(1000):\n",
    "    x=np.random.random()\n",
    "    if x<=0.5:\n",
    "        list_ran.append(\"a\")\n",
    "    if x>0.5 and x<=0.7:\n",
    "        list_ran.append(\"b\")\n",
    "    if x>0.7:\n",
    "        list_ran.append(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'c',\n",
       " 'b',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " 'b',\n",
       " 'c',\n",
       " 'c',\n",
       " 'a',\n",
       " 'b',\n",
       " 'b',\n",
       " 'a',\n",
       " 'a',\n",
       " 'c',\n",
       " 'c',\n",
       " 'b',\n",
       " ...]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_ran"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array(['a', 'b', 'c'], dtype='<U1'), array([521, 202, 287]))"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(list_ran,return_counts=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "np.unique?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=np.random.multivariate_normal([1.0,0.5],[[1.0,0],[0,1.5]],1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "x and y must be the same size",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-18-92b45543b774>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/.local/lib/python3.6/site-packages/matplotlib/pyplot.py\u001b[0m in \u001b[0;36mscatter\u001b[0;34m(x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, data, **kwargs)\u001b[0m\n\u001b[1;32m   2839\u001b[0m         \u001b[0mverts\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mverts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0medgecolors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0medgecolors\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2840\u001b[0m         plotnonfinite=plotnonfinite, **({\"data\": data} if data is not\n\u001b[0;32m-> 2841\u001b[0;31m         None else {}), **kwargs)\n\u001b[0m\u001b[1;32m   2842\u001b[0m     \u001b[0msci\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__ret\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2843\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0m__ret\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.6/site-packages/matplotlib/__init__.py\u001b[0m in \u001b[0;36minner\u001b[0;34m(ax, data, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1587\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0minner\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1588\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mdata\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1589\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msanitize_sequence\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1590\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1591\u001b[0m         \u001b[0mbound\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnew_sig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.6/site-packages/matplotlib/axes/_axes.py\u001b[0m in \u001b[0;36mscatter\u001b[0;34m(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, **kwargs)\u001b[0m\n\u001b[1;32m   4434\u001b[0m         \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mravel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4435\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4436\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"x and y must be the same size\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4437\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4438\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0ms\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: x and y must be the same size"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAD8CAYAAAB0IB+mAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAANT0lEQVR4nO3cYYjkd33H8ffHO1NpjKb0VpC706T00njYQtIlTRFqirZc8uDugUXuIFgleGAbKVWEFEuU+MiGWhCu1ZOKVdAYfSALntwDjQTEC7chNXgXItvTeheFrDHNk6Ax7bcPZtKdrneZf3Zndy/7fb/gYP7/+e3Mlx97752d2ZlUFZKk7e8VWz2AJGlzGHxJasLgS1ITBl+SmjD4ktSEwZekJqYGP8lnkzyZ5PuXuD5JPplkKcmjSW6c/ZiSpPUa8gj/c8CBF7n+VmDf+N9R4F/WP5YkadamBr+qHgR+/iJLDgGfr5FTwNVJXj+rASVJs7FzBrexGzg/cXxhfO6nqxcmOcrotwCuvPLKP7z++utncPeS1MfDDz/8s6qaW8vXziL4g1XVceA4wPz8fC0uLm7m3UvSy16S/1zr187ir3SeAPZOHO8Zn5MkXUZmEfwF4F3jv9a5GXimqn7t6RxJ0taa+pROki8BtwC7klwAPgK8EqCqPgWcAG4DloBngfds1LCSpLWbGvyqOjLl+gL+emYTSZI2hO+0laQmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqYlBwU9yIMnjSZaS3HWR69+Q5IEkjyR5NMltsx9VkrQeU4OfZAdwDLgV2A8cSbJ/1bK/B+6vqhuAw8A/z3pQSdL6DHmEfxOwVFXnquo54D7g0Ko1BbxmfPm1wE9mN6IkaRaGBH83cH7i+ML43KSPArcnuQCcAN5/sRtKcjTJYpLF5eXlNYwrSVqrWb1oewT4XFXtAW4DvpDk1267qo5X1XxVzc/Nzc3oriVJQwwJ/hPA3onjPeNzk+4A7geoqu8CrwJ2zWJASdJsDAn+aWBfkmuTXMHoRdmFVWt+DLwNIMmbGAXf52wk6TIyNfhV9TxwJ3ASeIzRX+OcSXJPkoPjZR8E3pvke8CXgHdXVW3U0JKkl27nkEVVdYLRi7GT5+6euHwWeMtsR5MkzZLvtJWkJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNTEo+EkOJHk8yVKSuy6x5p1JziY5k+SLsx1TkrReO6ctSLIDOAb8GXABOJ1koarOTqzZB/wd8JaqejrJ6zZqYEnS2gx5hH8TsFRV56rqOeA+4NCqNe8FjlXV0wBV9eRsx5QkrdeQ4O8Gzk8cXxifm3QdcF2S7yQ5leTAxW4oydEki0kWl5eX1zaxJGlNZvWi7U5gH3ALcAT4TJKrVy+qquNVNV9V83NzczO6a0nSEEOC/wSwd+J4z/jcpAvAQlX9qqp+CPyA0Q8ASdJlYkjwTwP7klyb5ArgMLCwas3XGD26J8kuRk/xnJvhnJKkdZoa/Kp6HrgTOAk8BtxfVWeS3JPk4HjZSeCpJGeBB4APVdVTGzW0JOmlS1VtyR3Pz8/X4uLilty3JL1cJXm4qubX8rW+01aSmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmBgU/yYEkjydZSnLXi6x7R5JKMj+7ESVJszA1+El2AMeAW4H9wJEk+y+y7irgb4CHZj2kJGn9hjzCvwlYqqpzVfUccB9w6CLrPgZ8HPjFDOeTJM3IkODvBs5PHF8Yn/s/SW4E9lbV11/shpIcTbKYZHF5efklDytJWrt1v2ib5BXAJ4APTltbVcerar6q5ufm5tZ715Kkl2BI8J8A9k4c7xmfe8FVwJuBbyf5EXAzsOALt5J0eRkS/NPAviTXJrkCOAwsvHBlVT1TVbuq6pqqugY4BRysqsUNmViStCZTg19VzwN3AieBx4D7q+pMknuSHNzoASVJs7FzyKKqOgGcWHXu7kusvWX9Y0mSZs132kpSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmhgU/CQHkjyeZCnJXRe5/gNJziZ5NMk3k7xx9qNKktZjavCT7ACOAbcC+4EjSfavWvYIMF9VfwB8FfiHWQ8qSVqfIY/wbwKWqupcVT0H3AccmlxQVQ9U1bPjw1PAntmOKUlaryHB3w2cnzi+MD53KXcA37jYFUmOJllMsri8vDx8SknSus30RdsktwPzwL0Xu76qjlfVfFXNz83NzfKuJUlT7Byw5glg78TxnvG5/yfJ24EPA2+tql/OZjxJ0qwMeYR/GtiX5NokVwCHgYXJBUluAD4NHKyqJ2c/piRpvaYGv6qeB+4ETgKPAfdX1Zkk9yQ5OF52L/Bq4CtJ/j3JwiVuTpK0RYY8pUNVnQBOrDp398Tlt894LknSjPlOW0lqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpow+JLUhMGXpCYMviQ1YfAlqQmDL0lNGHxJasLgS1ITBl+SmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElqwuBLUhMGX5KaMPiS1ITBl6QmDL4kNWHwJakJgy9JTRh8SWrC4EtSEwZfkpoYFPwkB5I8nmQpyV0Xuf43knx5fP1DSa6Z9aCSpPWZGvwkO4BjwK3AfuBIkv2rlt0BPF1Vvwv8E/DxWQ8qSVqfIY/wbwKWqupcVT0H3AccWrXmEPBv48tfBd6WJLMbU5K0XjsHrNkNnJ84vgD80aXWVNXzSZ4Bfhv42eSiJEeBo+PDXyb5/lqG3oZ2sWqvGnMvVrgXK9yLFb+31i8cEvyZqarjwHGAJItVNb+Z93+5ci9WuBcr3IsV7sWKJItr/dohT+k8AeydON4zPnfRNUl2Aq8FnlrrUJKk2RsS/NPAviTXJrkCOAwsrFqzAPzl+PJfAN+qqprdmJKk9Zr6lM74Ofk7gZPADuCzVXUmyT3AYlUtAP8KfCHJEvBzRj8Upjm+jrm3G/dihXuxwr1Y4V6sWPNexAfiktSD77SVpCYMviQ1seHB92MZVgzYiw8kOZvk0STfTPLGrZhzM0zbi4l170hSSbbtn+QN2Ysk7xx/b5xJ8sXNnnGzDPg/8oYkDyR5ZPz/5LatmHOjJflskicv9V6ljHxyvE+PJrlx0A1X1Yb9Y/Qi738AvwNcAXwP2L9qzV8BnxpfPgx8eSNn2qp/A/fiT4HfHF9+X+e9GK+7CngQOAXMb/XcW/h9sQ94BPit8fHrtnruLdyL48D7xpf3Az/a6rk3aC/+BLgR+P4lrr8N+AYQ4GbgoSG3u9GP8P1YhhVT96KqHqiqZ8eHpxi952E7GvJ9AfAxRp/L9IvNHG6TDdmL9wLHquppgKp6cpNn3CxD9qKA14wvvxb4ySbOt2mq6kFGf/F4KYeAz9fIKeDqJK+fdrsbHfyLfSzD7kutqarngRc+lmG7GbIXk+5g9BN8O5q6F+NfUfdW1dc3c7AtMOT74jrguiTfSXIqyYFNm25zDdmLjwK3J7kAnADevzmjXXZeak+ATf5oBQ2T5HZgHnjrVs+yFZK8AvgE8O4tHuVysZPR0zq3MPqt78Ekv19V/7WlU22NI8Dnquofk/wxo/f/vLmq/merB3s52OhH+H4sw4ohe0GStwMfBg5W1S83abbNNm0vrgLeDHw7yY8YPUe5sE1fuB3yfXEBWKiqX1XVD4EfMPoBsN0M2Ys7gPsBquq7wKsYfbBaN4N6stpGB9+PZVgxdS+S3AB8mlHst+vztDBlL6rqmaraVVXXVNU1jF7POFhVa/7QqMvYkP8jX2P06J4kuxg9xXNuM4fcJEP24sfA2wCSvIlR8Jc3dcrLwwLwrvFf69wMPFNVP532RRv6lE5t3McyvOwM3It7gVcDXxm/bv3jqjq4ZUNvkIF70cLAvTgJ/HmSs8B/Ax+qqm33W/DAvfgg8Jkkf8voBdx3b8cHiEm+xOiH/K7x6xUfAV4JUFWfYvT6xW3AEvAs8J5Bt7sN90qSdBG+01aSmjD4ktSEwZekJgy+JDVh8CWpCYMvSU0YfElq4n8BzPZcum6w2goAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x[:0],x[:1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig=plt.figure()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "int() argument must be a string, a bytes-like object or a number, not 'tuple'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-21-a8676c0299b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0max1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd_subplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0max1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'y'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.6/site-packages/matplotlib/figure.py\u001b[0m in \u001b[0;36madd_subplot\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1412\u001b[0m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_axstack\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1413\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1414\u001b[0;31m             \u001b[0ma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msubplot_class_factory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprojection_class\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1415\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1416\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_add_axes_internal\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.6/site-packages/matplotlib/axes/_subplots.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, fig, *args, **kwargs)\u001b[0m\n\u001b[1;32m     37\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m                     \u001b[0ms\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m                     \u001b[0mrows\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcols\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: int() argument must be a string, a bytes-like object or a number, not 'tuple'"
     ]
    }
   ],
   "source": [
    "ax1=fig.add_subplot((1,2,1))\n",
    "ax1.scatter(x[:0],x[:1],c='y')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}