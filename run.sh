#!/bin/bash

echo "REGISTER user1"
echo "CREATE_LISTING user1 'Phone model 8' 'Black color, brand new' 1000 'Electronics'"
echo "GET_LISTING user1 100001"
echo "CREATE_LISTING user1 'Black shoes' 'Training shoes' 100 'Sports'"
echo "REGISTER user2"
echo "REGISTER user2"
echo "CREATE_LISTING user2 'T-shirt' 'White color' 20 'Sports'"
echo "GET_LISTING user1 100003"
echo "GET_CATEGORY user1 'Fashion' sort_time asc"
echo "GET_CATEGORY user1 'Sports' sort_time dsc"
echo "GET_CATEGORY user1 'Sports' sort_price dsc"
echo "GET_TOP_CATEGORY user1"
echo "DELETE_LISTING user1 100003"
echo "DELETE_LISTING user2 100003"
echo "GET_TOP_CATEGORY user2"
echo "DELETE_LISTING user1 100002"
echo "GET_TOP_CATEGORY user1"
echo "GET_TOP_CATEGORY user3"