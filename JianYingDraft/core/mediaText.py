"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import json

from JianYingDraft.core import template
from JianYingDraft.core.media import Media
from JianYingDraft.utils import tools
from JianYingDraft.utils.dataStruct import SubtitleFontData
from JianYingDraft.utils.jsonCustionEncoder import JsonCustomEncoder


class MediaText(Media):
    def __init__(self, text, font_info=None):
        super().__init__()
        self.font_info = font_info
        self.text = text
    pass

    def _set_material_data_for_content(self):
        ma_id = tools.generate_id()

        self.material_data_for_content['material_animations'] = template.get_speed(ma_id)

        self.material_data_for_content["texts"] = self.__generate_text()
        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [ma_id, ]

    def __generate_text(self):
        _self = self
        entity = template.get_text(self.id)

        content = template.get_subtitle_content(self.text, font_info=self.font_info)

        entity["content"] = json.dumps(content, cls=JsonCustomEncoder)

        return entity

    def change_color(self, color):
        """
        改变文字颜色
        :param color: 以“#”开头后跟6位的颜色值
        """
        self.material_data_for_content['text_color'] = color
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        color1 = "<color=(1.000000, 1.000000, 1.000000, 1.000000)>"
        color2 = F'<color=({round(r / 255, 6):.6f}, {round(g / 255, 6):.6f}, {round(b / 255, 6):.6f}, 1.000000)>'
        self.material_data_for_content['content'] = self.material_data_for_content['content'].replace(color1, color2)


pass
