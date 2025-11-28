---
id: 207
title: "אז מה הקשר בין אוטומטים ופונקציות יוצרות?"
date: 2009-09-10 16:00:41
layout: post
categories: 
  - חישוביות
  - קומבינטוריקה
---
בפוסטים הקודמים <a href="http://www.gadial.net/2009/08/30/finite_automata_and_regular_languages/">תיארתי אוטומטים סופיים </a>ו<a href="http://www.gadial.net/2009/09/08/generating_functions/">תיארתי פונקציות יוצרות</a>. עכשיו הגיע הזמן להציג את הקשר היפה (לדעתי) בין השניים. שני הפוסטים הקודמים היו מעין מבוא מרפרף, ולכן בפוסט הזה ארשה לעצמי להיות פחות "מבואי" ולדבר יותר לעניין - ולכן הפוסט יהיה גם יותר טכני מהקודמים. ראו הוזהרתם.

ובכן, אם יש לנו שפה רגולרית {% equation %}L{% endequation %}, אפשר לשכוח מהמבנה הפנימי העשיר שלה ולהתמקד בשאלה כמותית - כמה מילים יש מכל אורך? נסמן ב-{% equation %}a_{n}{% endequation %} את מספר המילים ב-{% equation %}L{% endequation %} מאורך {% equation %}n{% endequation %}. אפשר כעת להתאים ל-{% equation %}L{% endequation %} פונקציה יוצרת {% equation %}f_{L}\left(x\right){% endequation %} שמתארת את הסדרה {% equation %}a_{n}{% endequation %} (למי שתוהה, יש מילה אחת מאורך 0 - "המילה הריקה", כך ש-{% equation %}a_{0}{% endequation %} יכול להיות שווה 1). כל זה טוב ויפה - כעת השאלה היא כיצד ניתן לחשב את {% equation %}f_{L}\left(x\right){% endequation %}. אציג שיטה כללית לעשות זאת, אם נתון אוטומט {% equation %}A{% endequation %} שמקבל את {% equation %}L{% endequation %}; זה מכתיב דרך פעולה כללית בהתמודדות עם בעיה קומבינטורית שאנחנו רוצים למצוא עבורה פונקציה יוצרת - קודם כל לבדוק האם הבעיה הזו ניתנת לניסוח בתור שפה רגולרית. אם כן, קיבלנו את הפונקציה היוצרת "בחינם".

מכיוון שאנחנו מתמקדים בשאלה כמותית ולא במבנה של כל מילה, אפשר להתעלם מההבדלים שבין אותיות שונות, ולהתמקד בשאלה יותר פשוטה הנוגעת לאוטומט - בכמה מסלולים שונים מאורך {% equation %}n{% endequation %} אפשר להגיע מהמצב ההתחלתי למצב המקבל? מספר המסלולים הזה הוא בדיוק {% equation %}a_{n}{% endequation %}. עם זאת, כפי שקורה בדרך כלל בהוכחות שעוסקות באוטומטים, צריך לשאול שאלה "חזקה" יותר - נניח שאנחנו מתחילים ממצב <strong>כלשהו</strong> של האוטומט, לאו דווקא המצב ההתחלתי. כמה מסלולים מאורך {% equation %}n{% endequation %} שמגיעים למצב מקבל יהיו כעת? אם {% equation %}q_{i}{% endequation %} הוא המצב הזה, אפשר לסמן את המספר בתור {% equation %}a_{n}^{i}{% endequation %}, ואת הפונקציה היוצרת המתאימה בתור {% equation %}f_{i}\left(x\right){% endequation %}. כדי לפשט עוד יותר את הסימונים אפשר לדבר על <strong>וקטור</strong> של פונקציות יוצרות: {% equation %}\overline{f}=\left(f_{0},f_{2},\dots,f_{k}\right){% endequation %} (אני מסמן את מספר המצבים הכולל של האוטומט ב-{% equation %}k+1{% endequation %} כדי שהוקטור יראה "נחמד").

מכיוון שויתרנו על זהות האותיות השונות ואנחנו מתמקדים רק במספר הדרכים להגיע ממצב אחד באוטומט לאחר, אפשר להפסיק לדבר על פונקצית המעברים של האוטומט ולהסתפק במעין טבלת מעברים מופשטת - מטריצה מגודל {% equation %}\left(k+1\right)\times\left(k+1\right){% endequation %} שהן שורותיה והן עמודותיה מייצגות מצבים, ובתא ה-{% equation %}\left(i,j\right){% endequation %} שלה כתוב מספר הדרכים לעבור מהמצב {% equation %}q_{i}{% endequation %} למצב {% equation %}q_{j}{% endequation %} (בצורה אולטרה פורמלית, זהו {% equation %}\left|\left\{ \sigma\in\Sigma:\delta\left(q_{i},\sigma\right)=q_{j}\right\} \right|{% endequation %}). דרך הייצוג הזו, של גרף באמצעות מטריצה, היא מאוד, מאוד נפוצה. אקרא למטריצה הזו {% equation %}T{% endequation %}. אלו שבקיאים באלגברה לינארית ומכירים כפל מטריצות יכולים לוודא לעצמם ש-{% equation %}T^{r}{% endequation %} היא המטריצה שבכניסה {% equation %}\left(i,j\right){% endequation %} שלה רשום מספר הדרכים להגיע מ-{% equation %}i{% endequation %} אל {% equation %}j{% endequation %} בדיוק ב-{% equation %}r{% endequation %} צעדים.

האבחנה הבסיסית בכל הסיפור הזה היא פשוטה ביותר. מספר המסלולים מאורך {% equation %}n{% endequation %} שמובילים מ-{% equation %}q_{i}{% endequation %} אל מצב מקבל כלשהו ניתן לחישוב באופן רקורסיבי. אם {% equation %}n=0{% endequation %} אז הוא 1 אם {% equation %}q_{i}{% endequation %} הוא בעצמו מצב מקבל ואחרת הוא 0. אפשר לסמן זאת בקומפקטיות באמצעות וקטור: {% equation %}\overline{u}{% endequation %}יהיה וקטור שבכניסה ה-{% equation %}i{% endequation %} שלו יש 1 אם המצב {% equation %}q_{i}{% endequation %} הוא מקבל, ואחרת 0. אם {% equation %}n&gt;0{% endequation %} אז אפשר להפעיל רקורסיה: לכל מצב {% equation %}q_{j}{% endequation %} אפשר לדבר על "מספר המסלולים מאורך {% equation %}n{% endequation %} מ-{% equation %}q_{i}{% endequation %} למצב מקבל, שבצעד הראשון נכנסים ל-{% equation %}q_{j}{% endequation %}". מספר המסלולים הללו הוא בדיוק המכפלה של מספר האפשרויות לעבור מ-{% equation %}q_{i}{% endequation %} אל {% equation %}q_{j}{% endequation %} (כלומר, {% equation %}T_{ij}{% endequation %}) במספר המסלולים מאורך {% equation %}n-1{% endequation %} מ-{% equation %}q_{j}{% endequation %} שמגיעים למצב מקבל. מכיוון ש<strong>כל</strong> מסלול מ-{% equation %}q_{i}{% endequation %} שמגיע למצב מקבל חייב לעבור דרך {% equation %}q_{j}{% endequation %} <strong>כלשהו</strong> בצעד הראשון, מספר המסלולים הכולל הוא סכום של המכפלות הללו, עבור כל ה-{% equation %}j{% endequation %}-ים האפשריים. מי שבקיא באלגברה לינארית אולי רואה כבר <a href="http://he.wikipedia.org/wiki/%D7%9B%D7%A4%D7%9C_%D7%9E%D7%98%D7%A8%D7%99%D7%A6%D7%95%D7%AA">כפל מטריצות</a> מול העיניים, אז אכתוב במפורש את הנוסחה: {% equation %}f_{i}\left(x\right) = u_{i}+\sum_{j}T_{ij}\cdot xf_{j}\left(x\right)=u_{i}+\left[T\right]_{i}\cdot x\overline{f}\left(x\right){% endequation %}

ההכפלה ב-{% equation %}x{% endequation %} של {% equation %}f_{j}\left(x\right){% endequation %} היא הדרך שלנו לבטא את העובדה שמסלול מאורך {% equation %}n{% endequation %} של {% equation %}f_{i}{% endequation %} נבנה באמצעות מסלולים מאורך {% equation %}n-1{% endequation %} של אגף ימין. ה-{% equation %}u_{i}{% endequation %} שמתווסף לסכום בא לתאר בדיוק את תנאי העצירה של הרקורסיה (הוא יהיה המקדם החופשי בטור של {% equation %}f_{i}\left(x\right){% endequation %}).

המשוואה שלמעלה היא משוואה כללית לכל {% equation %}i{% endequation %}; היא בעצם מייצגת מערכת של {% equation %}k+1{% endequation %} משוואות. את כל המערכת הזו אפשר לתאר באופן עוד יותר קומפקטי:

{% equation %}\overline{f} = u+T\cdot x\overline{f}{% endequation %}

ועל ידי העברת אגף מקבלים:

{% equation %}\overline{f}\left(I-xT\right) = u{% endequation %}

ומכאן:

{% equation %}\overline{f} = \left(I-xT\right)^{-1}u{% endequation %}

וזה נותן לנו את וקטור הפונקציות היוצרות עבור כל המצבים. אם רוצים "לבודד" את הפונקציה היוצרת רק עבור המצב {% equation %}q_{0}{% endequation %}, צריך לכפול את שני האגפים בוקטור {% equation %}\left(1,0,0,\dots,0\right){% endequation %} (הוקטור שכולו אפסים פרט לכניסה במקום ה-0). נסמן וקטור זה כ-{% equation %}v{% endequation %}, ונקבל ש-{% equation %}f_{0}\left(x\right)=v\left(I-xT\right)^{-1}u{% endequation %}. זו הנוסחה.

חישוב של כל העסק הזה הוא לא מסובך, בהינתן שאנחנו כבר יודעים לעשות חשבון עם פולינומים. יש מערכות אלגברה ממוחשבות שעושות את זה בדיוק - אני משתמש ב-<a href="http://www.sagemath.org/">Sage</a> לצורך כך, ובה החישוב שלעיל הוא מיידי. התוצאה המתקבלת היא תמיד פונקציה רציונלית (מנה של שני פולינומים), כך שמציאת נקודות הסינגולריות שלה (הנקודות שבהן "משהו מתקלקל" ולכן אפשר ללמוד מהן על קצב הגידול של {% equation %}a_{n}{% endequation %}) היא פשוטה למדי (אלו בדיוק הנקודות שמאפסות את המכנה).

זה הכל. אחרי ההקדמה הארוכה שנתתי, הפשטות והמיידיות של התוצאה הן לטעמי יפות מאוד, כך שלא אכביר עליהן עוד מילים. מן הסתם נפנפתי פה בידיים ללא הרף ויש נקודות עדינות שעוד דורשות התייחסות, אך למזלי אני יכול להרשות לעצמי כאן להיות לא מדויק.
