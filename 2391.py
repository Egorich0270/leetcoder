class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_time, g_path = 0, 0
        m_time, m_path = 0, 0
        p_time, p_path = 0, 0
        for i, trash in enumerate(garbage):
            g, m, p = 0, 0, 0
            for x in trash:
                match x:
                    case 'G':
                        g += 1
                    case 'M':
                        m += 1
                    case 'P':
                        p += 1
            if g:
                g_time += g + g_path
                g_path = 0
            if m:
                m_time += m + m_path
                m_path = 0
            if p:
                p_time += p + p_path
                p_path = 0
            if i < len(travel):
                g_path += travel[i]
                m_path += travel[i]
                p_path += travel[i]
        return p_time + m_time + g_time


