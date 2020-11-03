FILE=$1
URL=$2

echo "Note: available models are photo2cartoon"

echo "Specified [$FILE]"

mkdir -p ./checkpoints/${FILE}_pretrained
MODEL_FILE=./checkpoints/${FILE}_pretrained/latest_net_G.pth
# URL=http://efrosgans.eecs.berkeley.edu/cyclegan/pretrained_models/$FILE.pth

wget -N $URL -O $MODEL_FILE