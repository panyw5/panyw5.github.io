#!/bin/bash

# 部署脚本：同步课件到网站
# 使用方法：./deploy.sh

set -e

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 网站根目录
SITE_DIR="$(cd "$(dirname "$0")" && pwd)"

# 课件源目录
MMP_SOURCE="/Users/lelouch/Nutstore Files/中大事务/中大教学/课程讲义/数学物理方法讲义"
GROUP_THEORY_SOURCE="/Users/lelouch/Nutstore Files/中大事务/中大教学/课程讲义/群论讲义"

# 目标目录
MMP_TARGET="$SITE_DIR/courses/mmp"
GROUP_THEORY_TARGET="$SITE_DIR/courses/group-theory"

echo -e "${YELLOW}开始同步课件...${NC}"

# 同步数学物理方法
if [ -d "$MMP_SOURCE" ]; then
    echo -e "同步: 数学物理方法"
    mkdir -p "$MMP_TARGET"
    rsync -av --delete \
        --exclude='MaPh_202208/' \
        --exclude='code/' \
        --exclude='deepseek/' \
        --exclude='参考教材/' \
        --exclude='题库/' \
        --exclude='.DS_Store' \
        --exclude='*.key' \
        --exclude='*.pptx' \
        --exclude='*.pdf' \
        --exclude='*.sty' \
        --exclude='*.css' \
        --include='*/' \
        --include='slides.html' \
        --include='slides.md' \
        --include='image/**' \
        --include='images/**' \
        --include='assets/**' \
        --include='media/**' \
        --exclude='*' \
        --prune-empty-dirs \
        "$MMP_SOURCE/" "$MMP_TARGET/"
    echo -e "${GREEN}✓ 数学物理方法同步完成${NC}"
else
    echo -e "${YELLOW}⚠ 数学物理方法源目录不存在: $MMP_SOURCE${NC}"
fi

# 同步群论
if [ -d "$GROUP_THEORY_SOURCE" ]; then
    echo -e "同步: 群论"
    mkdir -p "$GROUP_THEORY_TARGET"
    rsync -av --delete \
        --exclude='.DS_Store' \
        --exclude='*.key' \
        --exclude='*.pptx' \
        --exclude='*.pdf' \
        --exclude='*.sty' \
        --exclude='*.css' \
        --include='*/' \
        --include='*.html' \
        --include='image/**' \
        --include='images/**' \
        --include='assets/**' \
        --include='media/**' \
        --exclude='*' \
        --prune-empty-dirs \
        "$GROUP_THEORY_SOURCE/" "$GROUP_THEORY_TARGET/"
    echo -e "${GREEN}✓ 群论同步完成${NC}"
else
    echo -e "${YELLOW}⚠ 群论源目录不存在: $GROUP_THEORY_SOURCE${NC}"
fi

echo ""
echo -e "${GREEN}同步完成！${NC}"
echo "现在可以运行: git add . && git commit -m 'Update slides' && git push"
