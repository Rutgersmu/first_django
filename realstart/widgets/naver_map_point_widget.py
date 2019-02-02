import re

from django import forms
from django.template.loader import render_to_string

from django.conf import settings # django/conf/global_settings.py (base) + realstart/settings.py (재정의)

class NaverMapPointWidget(forms.TextInput):
    def render(self, name, value, attrs, renderer=None): # renderer 추가 안 하면 오류 뜸
        width = str(self.attrs.get('width', 800))
        height = str(self.attrs.get('height', 600)) # 있으면 가져오고 없으면 600
        if width.isdigit(): width += 'px'
        if height.isdigit(): height += 'px'


        context = {
            'naver_clint_id': settings.NAVER_CLIENT_ID,
            'id':attrs['id'],
            'width': width, 'height': height,
            'base_lat': self.BASE_LAT, 'base_lng': self.BASE_LNG        }

        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lat': lat, 'base_lng': lng})
            except (IndexError, ValueError):
                pass

        attrs['readonly'] = 'readonly' # 읽기전용 부모 호출되기 전에 -> 수정 불가
        parent_html = super().render(name, value, attrs)
        html = render_to_string('widgets/naver_map_point_widget.html', context)
        return parent_html + html


