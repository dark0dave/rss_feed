#!/usr/bin/env bash

input_file=$1

sed 's/></>\n</g' ${input_file} > feed.opml
