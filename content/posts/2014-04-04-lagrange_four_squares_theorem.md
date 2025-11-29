---
id: 3090
title: "משפט ארבעת הריבועים של לגראנז'"
date: 2014-04-04 11:29:36
layout: post
categories: 
  - תורת המספרים
tags: 
  - גם טכני זה כיף!
  - הוכחות
  - משפט ארבעת הריבועים של לגראנז'
  - סכומי ריבועים
  - קווטרניונים
social_media_share: true
---
אני רוצה לדבר על אחת מהתוצאות הנחמדות ביותר (לטעמי) בתורת המספרים האלמנטרית - משפט ארבעת הריבועים של לגראנז'. בפשטות, המשפט אומר שאפשר להציג כל מספר טבעי בתור סכום של ארבעה ריבועים של מספרים טבעיים (כש-0 נחשב למספר טבעי). הנה דוגמאות עבור המספרים הטבעיים מ-1 עד 7:

{% equation %}1=1^{2}+0^{2}+0^{2}+0^{2}{% endequation %}

{% equation %}2=1^{2}+1^{2}+0^{2}+0^{2}{% endequation %}

{% equation %}3=1^{2}+1^{2}+1^{2}+0^{2}{% endequation %}

{% equation %}4=2^{2}+0^{2}+0^{2}+0^{2}{% endequation %}

{% equation %}5=2^{2}+1^{2}+0^{2}+0^{2}{% endequation %}

{% equation %}6=2^{2}+1^{2}+1^{2}+0^{2}{% endequation %}

{% equation %}7=2^{2}+1^{2}+1^{2}+1^{2}{% endequation %}

הפסקתי ב-7 בכוונה - הוא הדוגמה הראשונה שיש לנו למספר שאנחנו <strong>חייבים</strong> ארבעה ריבועים כדי לקבל אותו (תוכיחו! זה בסך הכל כולל בדיקה של כמה מקרים). מה שמפתיע כאן הוא ש-4 זה <strong>כל מה שצריך</strong> - ואפשר לייצג כל מספר, גדול ומורכב ככל שיהיה, כסכום של ארבעה ריבועים.

כשאני אומר שזה משפט בתורת המספרים "האלמנטרית" הכוונה היא לכך שלא משתמשים בכלים מתמטיים כבדים שנדרשת היכרות מוקדמת איתם - ההוכחה מסתמכת על <a href="http://www.gadial.net/2013/05/13/modular_arithmetic/">חשבון מודולורי</a> ותו לא (וחשבון מודולורי הוא לגמרי הלחם והחמאה של תורת המספרים). זה לא אומר שההוכחה היא אלמנטרית, למרות שהיא לא מסובכת במיוחד; הפוסט הזה כן יהיה טכני, וקשה יהיה להבין את ההוכחה בלי להתעמק קצת בפרטים הטכניים הללו. וזה בסדר גמור ואין עם זה בעיה - בלי להתעסק בפרטים הטכניים מפספסים לא מעט מהכיף שבמתמטיקה, לטעמי.

את ההוכחה עצמה אפשר לחלק לשני חלקים: ראשית, מראים שאפשר לצמצם את הבעיה כך שמספיק להוכיח שכל מספר <strong>ראשוני</strong> ניתן להצגה כסכום של ארבעה ראשונים; ואז מראים את זה עבור ראשוניים. הרדוקציה הזו ל"מספיק להוכיח על ראשוניים" היא לכשעצמה טכניקה נפוצה בתורת המספרים והיא עובדת יפה גם כאן (כי יותר קל להוכיח עבור ראשוני שהוא סכום של ארבעה ריבועים מאשר עבור מספר כללי). אז בואו נתחיל קודם כל מהחלק הראשון - לשכנע אתכם שמספיק להוכיח שכל ראשוני הוא סכום של ארבעה ריבועים.

הטענה שאני רוצה להוכיח היא זו: אם {% equation %}a{% endequation %} ניתן להצגה כסכום של ארבעה ריבועים, ו-{% equation %}b{% endequation %} ניתן להצגה כסכום של ארבעה ריבועים, אז גם {% equation %}ab{% endequation %} (המכפלה שלהם) ניתן להצגה כסכום של ארבעה ריבועים. נשמע לכם טריוויאלי או מובן מאליו? אין בעיה - קחו דקה בצד ונסו להוכיח את זה. כנראה שתגלו שזה לא פשוט כמו שזה נראה.

אם הוכחתי את הטענה הזו, אז נובע מייד שמספיק להוכיח את המשפט עבור ראשוניים. למה? ובכן, ראשית, טריוויאלי להכליל את הטענה עבור מכפלה של מספר סופי של מספרים (כלומר, המכפלה של כל מספר סופי של מספרים, שכולם סכום של ארבעה ריבועים, גם היא סכום של ארבעה ריבועים). שנית, כל מספר גדול מ-1 הוא מכפלה של מספר סופי של ראשוניים, ולכן אם כל הראשוניים הם סכום של ארבעה ריבועים, כל מספר הוא כזה (למעט 0 ו-1 אבל כבר ראינו מה קורה איתם). הנה דוגמה קלאסית לאופן שבו היות הראשוניים "אבני הבניין" של כל המספרים עוזר לנו.

ובכן, נניח ש-{% equation %}a,b{% endequation %} הם סכום של ארבעה ריבועים. למה גם {% equation %}ab{% endequation %} כזה? התשובה: זה כואב. מה כואב? לראות את הנוסחה המתאימה. מה שעושים הוא לכתוב הצגה של {% equation %}a{% endequation %} כסכום של ארבעה ריבועים, ואת {% equation %}b{% endequation %} כסכום של ארבעה ריבועים, ואז לכתוב את הביטוי המדויק שמתאר את {% equation %}ab{% endequation %} בתור סכום של ארבעה ריבועים. אפשר לפתוח סוגריים ולראות שהכל יוצא כמו שצריך, אבל זה כואב. כמו כן, מי זוכר איך בכלל הנוסחה הזו נראית? האם אני צריך לזכור את הנוסחה בעל פה? ממתי צריך לזכור דברים במתמטיקה בעל פה? האם אני יכול לכתוב את החלק הזה של הפוסט מהראש בלי להעתיק מספר? ובכן, יש תעלול אחד שיקל עלי את החיים, ויתן לי תירוץ להציג מושג חדש ומעניין בפני עצמו: קווטרניונים.

לקווטרניונים היסטוריה מרתקת משל עצמם אבל לא אכנס אליה כרגע. הרעיון הבסיסי בהם הוא להרחיב בצורה מסויימת את המספרים המרוכבים. אם המספרים המרוכבים הם מספרים מהצורה {% equation %}a+bi{% endequation %} כאשר {% equation %}a,b\in\mathbb{R}{% endequation %} ו-{% equation %}i{% endequation %} מקיים ש-{% equation %}i^{2}=-1{% endequation %}, אז הקווטרניונים (מעל הממשיים; יש מושג כללי יותר של אלגברת קווטרניונים שלא אכנס אליו כאן) הם מספרים מהצורה {% equation %}a+bi+cj+dk{% endequation %} כאשר {% equation %}a,b,c,d\in\mathbb{R}{% endequation %} ו-{% equation %}i^{2}=j^{2}=k^{2}=-1{% endequation %}, והמכפלות של {% equation %}i,j,k{% endequation %} מתוארות על ידי הכלל "כפל על פי הסדר נותן את הבא בתור, וכפל בסדר הפוך נותן את המינוס שלו". מה זאת אומרת? הנה המשוואות:

{% equation %}ij=k{% endequation %} ו-{% equation %}ji=-k{% endequation %}

{% equation %}jk=i{% endequation %} ו-{% equation %}kj=-i{% endequation %}

{% equation %}ki=j{% endequation %} ו-{% equation %}ik=-j{% endequation %}

(למעשה, מספיקות רק המשוואות {% equation %}ij=k,jk=i,ki=j{% endequation %} והמשוואה {% equation %}i^{2}=j^{2}=k^{2}=-1{% endequation %} כדי שניתן יהיה להסיק את היתר).

הנה דוגמה פשוטה למכפלה של שני קווטרניונים:

{% equation %}\left(4+3i\right)\left(2+5k\right)=8+6i+20k+15ik=8+6i-15j+20k{% endequation %}

עכשיו, למספרים מרוכבים יש <strong>נורמה</strong>, שהיא מדד ל"גודל" שלהם (פורמלית - המרחק של המספר המרוכב מראשית הצירים). הנורמה מסומנת בסימן של ערך מוחלט, ומוגדרת בתור {% equation %}\left|a+bi\right|=\sqrt{a^{2}+b^{2}}{% endequation %}, או {% equation %}\left|a+bi\right|^{2}=a^{2}+b^{2}{% endequation %}. תכונה חשובה של הנורמה הזו היא שהיא <strong>כפלית</strong>, כלומר {% equation %}\left|a+bi\right|\left|x+yi\right|=\left|\left(a+bi\right)\left(x+yi\right)\right|{% endequation %}. הרעיון הוא שעם קווטרניונים זה אותו הדבר בדיוק.

איך זה קשור לענייננו? ובכן, אם {% equation %}a+bi+cj+dk{% endequation %} הוא קווטרניון, אז הנורמה שלו בריבוע היא בדיוק {% equation %}a^{2}+b^{2}+c^{2}+d^{2}{% endequation %}, כלומר סכום של ארבעה ריבועים. ולהפך: לכל ארבעה מספרים שנרצה, אפשר לבנות קווטרניון שהנורמה שלו בריבוע היא סכום הריבועים של המספרים (פשוט לוקחים את המספרים להיות מקדמי הקווטרניון). כעת, אם {% equation %}p,q{% endequation %} הם קווטרניונים, אז המשוואה {% equation %}\left|p\right|^{2}\left|q\right|^{2}=\left|pq\right|^{2}{% endequation %} אומרת לנו בדיוק שמכפלת שני סכומים ארבעה ריבועים ({% equation %}\left|p\right|^{2}{% endequation %} ו-{% equation %}\left|q\right|^{2}{% endequation %}) היא בעצמה סכום של ארבעה ריבועים ({% equation %}\left|pq\right|^{2}{% endequation %}).

כעת ברור גם איך אפשר למצוא את הנוסחה במפורש: ניקח את {% equation %}\left(a+bi+cj+dk\right){% endequation %} ונכפול אותו ב-{% equation %}\left(x+yi+zj+uk\right){% endequation %}, ונבדוק את הנורמה של מה שנקבל. זה לא יהיה נעים. זה יהיה כואב. אבל לפחות לא אצטרך להעתיק נוסחה משום מקום ואוכל לפתח את הכל בעצמי - ותאמינו לי, זה מרגיש יותר טוב.

ובכן:

{% equation %}\left(a+bi+cj+dk\right)\left(x+yi+zj+uk\right)=\left(ax-by-cz-du\right)+{% endequation %}

{% equation %}\left(ay+bx+cu-dz\right)i+\left(az-bu+cx+dy\right)j+\left(au+bz-cy+dx\right)k{% endequation %}

ולכן קיבלתי את הנוסחה הבאה להצגה של מכפלת שני סכומי ארבעה ריבועים כסכום של ארבעה ריבועים:

{% equation %}\left(a^{2}+b^{2}+c^{2}+d^{2}\right)\left(x^{2}+y^{2}+z^{2}+u^{2}\right)={% endequation %}

{% equation %}\left(ax-by-cz-du\right){}^{2}+\left(ay+bx+cu-dz\right)^{2}+\left(az-bu+cx+dy\right)^{2}+\left(au+bz-cy+dx\right)^{2}{% endequation %}

עדיין לא הוכחתי שהנוסחה נכונה, כי הסתמכתי על ההנחה שהנורמה של הקווטרניונים כפלית - אבל כאמור, מרגע שיש לנו את הנוסחה מול העיניים אפשר סתם לפתוח את הסוגריים ולראות שהיא עובדת. למי שבכל זאת רוצה דרך עקיפה, אפשר להסתמך על כך שקווטרניונים ניתנים לייצוג על ידי מטריצות מסדר {% equation %}2\times2{% endequation %} מעל המרוכבים, באופן הבא: המספר {% equation %}a+bi+cj+dk{% endequation %} מיוצג על ידי המטריצה {% equation %}\left[\begin{array}{cc}a+bi & c+di\\-c+di & a-bi\end{array}\right]{% endequation %}. כמובן, עכשיו צריך לבדוק שהייצוג הזה באמת נכון (כלומר, לכפול שתי מטריצות ולראות שמתקבלת המכפלה שציפינו לה), אבל מרגע שבדקנו את זה, סיימנו: הנורמה של הקווטרניון היא פשוט הדטרמיננטה של המטריצה (לראות את זה - זה מיידיי לחלוטין) ודטרמיננטה של מטריצות היא כפלית.

איבדתם אותי? גם אם כן, לא נורא - זה לא פוסט על קווטרניונים ולא חייבים להבין את מה שעשיתי פה בשביל ההמשך - כל מה שחשוב הוא שמכאן והלאה מספיק לנו להוכיח את משפט לגראנז' עבור ראשוניים בלבד. וכאן אנחנו מתחילים להשתמש בטיעוני תורת המספרים.

המתווה של ההוכחה מעתה והלאה הוא זה: יהא {% equation %}p{% endequation %} מספר ראשוני אי זוגי כלשהו (ב-2 כבר טיפלנו במפורש קודם, ובהמשך הוא יעשה בעיות כפי שהוא בדרך כלל עושה אז נניח ש-{% equation %}p{% endequation %} שונה ממנו). בשלב ראשון אני אמצא מספר {% equation %}1\le m<p{% endequation %} כלשהו כך ש-{% equation %}mp{% endequation %}הוא סכום של ארבעה ריבועים - זה יהיה די קל, באופן אולי מפתיע. לדוגמה, נניח שאני רוצה להוכיח ש-13 הוא סכום של 4 ריבועים, אני אתחיל מלהוכיח ש-65 (ששווה ל-{% equation %}13\cdot5{% endequation %}) הוא סכום של ארבעה ריבועים כי קל לי לראות את זה: {% equation %}65=8^{2}+1^{2}+0^{2}+0^{2}{% endequation %}. עכשיו, אחרי שמצאתי {% equation %}m{% endequation %} כזה, אני רוצה להתחיל "להצטמצם". אני אוכיח שאם יש {% equation %}1<m&lt;p{% endequation %} כך ש-{% equation %}mp{% endequation %} הוא סכום של ארבעה ריבועים, אז קיים {% equation %}1\le n<m{% endequation %} כך ש-{% equation %}np{% endequation %} הוא עדיין סכום של ארבעה ריבועים - כלומר, הקטנתי את מי שמוכפל ב-{% equation %}p{% endequation %}. ואז אני יכול לחזור על ההוכחה הזו גם עבורו, ושוב ושוב עד שלבסוף בהכרח אגיע ל-{% equation %}p{% endequation %} עצמו (כלומר, כשהוא מוכפל ב-1). ההוכחה של השלב הזה - הנסיגה הזו כלפי מטה - היא החלק הקשה והטכני ביותר בהוכחה (אבל לא לדאוג, גם הוא לא כל כך נורא).

כדי להוכיח שקיים {% equation %}m<p{% endequation %} כך ש-{% equation %}mp{% endequation %} הוא סכום של ארבעה ריבועים, אני אסתכל על {% equation %}\mathbb{Z}_{p}{% endequation %} - שדה המספרים מודולו {% equation %}p{% endequation %}, ואוכיח שיש בו פתרון למשוואה {% equation %}x^{2}+y^{2}+1=0{% endequation %}, כלומר ש-{% equation %}p|x^{2}+y^{2}+1{% endequation %}, כלומר שקיים {% equation %}m{% endequation %} כך ש-{% equation %}mp=x^{2}+y^{2}+1=x^{2}+y^{2}+1^{2}+0^{2}{% endequation %}, ואם יהיה לי חסם טוב כלשהו על הגודל של {% equation %}x,y{% endequation %} אז גם אוכל לחסום את הגודל של {% equation %}m{% endequation %}. זה המקום הראשון שבו העובדה שהצטמצמנו לדיבור על ראשוני {% equation %}p{% endequation %} עוזרת; למשל, ב-{% equation %}\mathbb{Z}_{8}{% endequation %} אין פתרון למשוואה הזו, כי {% equation %}x^{2}{% endequation %} מודולו 8 יכול להיות רק 0 או 1 או 4. אז מה ההבדל בין ראשוני ולא ראשוני? ב-{% equation %}\mathbb{Z}_{8}{% endequation %} מה שקורה הוא שיש ארבעה מספרים שבריבוע נותנים 1 - 1,3,5,7, כלומר ל-1 יש ארבעה שורשים; לעומת זאת, עבור {% equation %}p{% endequation %} ראשוני לכל מספר יש לכל היותר שני שורשים - זה נובע מכך ש-{% equation %}\mathbb{Z}_{p}{% endequation %} הוא שדה ולכן לפולינום ממעלה {% equation %}n{% endequation %} מעל {% equation %}\mathbb{Z}_{p}{% endequation %} יש לכל היותר {% equation %}n{% endequation %} שורשים (ולכן לפולינום {% equation %}x^{2}-a{% endequation %} יש לכל היותר שני שורשים, כלומר ל-{% equation %}a{% endequation %} יש לכל היותר שני שורשים).

ספציפית ב-{% equation %}\mathbb{Z}_{p}{% endequation %}, ל-0 יש רק שורש אחד (0) ולכל מספר אחר שהוא ריבוע יש בדיוק שני שורשים (אם {% equation %}a=x^{2}{% endequation %} אז {% equation %}y=-x{% endequation %} גם הוא שורש כי {% equation %}y^{2}=\left(-x\right)^{2}=x^{2}=a{% endequation %}, ולא ייתכן ש-{% equation %}x=y{% endequation %} כי אם {% equation %}x=-x{% endequation %} אז {% equation %}2x=0{% endequation %} מודולו {% equation %}p{% endequation %} ולכן {% equation %}p{% endequation %} מחלק את 2). זה אומר שאם נגדיר את הקבוצה {% equation %}S=\left\{ a^{2}\ |\ a\in\mathbb{Z}_{p}\right\} {% endequation %}, גודלה יהיה בדיוק {% equation %}\frac{p+1}{2}{% endequation %}. למה? כי בואו ניקח את כל המספרים ב-{% equation %}\mathbb{Z}_{p}{% endequation %} ונעלה אותם בריבוע. 0 הוא מקרה מיוחד, ופרט אליו נשארים {% equation %}p-1{% endequation %} איברים שאפשר לסדר בזוגות שנותנים את אותו ריבוע, כלומר נקבל {% equation %}\frac{p-1}{2}+1{% endequation %} ריבועים בסך הכל, וזה שווה ל-{% equation %}\frac{p+1}{2}{% endequation %}.

עכשיו בואו נביט שוב על המשוואה שאנו רוצים לפתור: {% equation %}x^{2}+y^{2}+1=0{% endequation %}, כלומר {% equation %}x^{2}=-1-y^{2}{% endequation %}. אם נצליח למצוא ריבוע שהוא גם מהצורה {% equation %}-1-y^{2}{% endequation %} ניצחנו; נגדיר {% equation %}S^{\prime}=\left\{ -1-a\ |\ a\in S\right\} {% endequation %}. אם {% equation %}a\ne b{% endequation %} אז {% equation %}-1-a\ne-1-b{% endequation %} ולכן גם הגודל של {% equation %}S^{\prime}{% endequation %} הוא {% equation %}\frac{p+1}{2}{% endequation %}. אז מה קיבלנו? שתי קבוצות: {% equation %}S,S^{\prime}{% endequation %}, שמספר האיברים הכולל בשתיהן הוא {% equation %}p+1{% endequation %}, אבל ב-{% equation %}\mathbb{Z}_{p}{% endequation %} יש בדיוק {% equation %}p{% endequation %} איברים. מסקנה: יש ל-{% equation %}S,S^{\prime}{% endequation %} איבר משותף - איבר שניתן להציג גם כ-{% equation %}x^{2}{% endequation %} וגם כ-{% equation %}-1-y^{2}{% endequation %}. לכן מצאנו שמתקיים {% equation %}x^{2}=-1-y^{2}{% endequation %}, כלומר {% equation %}x^{2}+y^{2}+1=0{% endequation %}, ומכאן שקיים {% equation %}m{% endequation %} כך ש-{% equation %}mp=x^{2}+y^{2}+1{% endequation %}. לכן בפרט {% equation %}mp{% endequation %} הוא סכום של ארבעה ריבועים: {% equation %}mp=x^{2}+y^{2}+1^{2}+0^{2}{% endequation %}.

אנחנו עדיין רוצים להגביל את הגודל של ה-{% equation %}m{% endequation %} הזה, ונעשה את זה עם תעלול סטנדרטי. אם {% equation %}p|x^{2}+y^{2}+1{% endequation %}, אז אפשר להוסיף או להחסיר {% equation %}p{% endequation %} בחופשיות ל-{% equation %}x,y{% endequation %} והמשוואה עדיין תתקיים ("להחליף את {% equation %}x{% endequation %} באיבר ששקול לו מודולו {% equation %}p{% endequation %}"). למשל, אם {% equation %}7|2^{2}+4^{2}+1{% endequation %}, אנחנו יכולים להחליף את {% equation %}4{% endequation %} ב-{% equation %}-3{% endequation %} ולקבל את אותו דבר: {% equation %}7|2^{2}+\left(-3\right)^{2}+1{% endequation %}. הסכום הראשון נותן לנו {% equation %}4+16+1=21{% endequation %} והסכום השני נותן לנו {% equation %}4+9+1=14{% endequation %} - שניהם מתחלקים ב-7, אבל שימו לב שהסכום השני קטן יותר. אז מה שנעשה עם המשוואה {% equation %}p|x^{2}+y^{2}+1{% endequation %} הכללית הוא לבחור את {% equation %}x{% endequation %} כך שיקיים {% equation %}\left|x\right|<\frac{p}{2}{% endequation %} וכך גם עבור {% equation %}y{% endequation %}. אם אתם לא משוכנעים שאפשר, נסו להוכיח זאת לעצמכם. המסקנה? אם {% equation %}mp=x^{2}+y^{2}+1{% endequation %} אז {% equation %}mp<\left(\frac{p}{2}\right)^{2}+\left(\frac{p}{2}\right)^{2}+1=\frac{p^{2}}{2}+1\le p^{2}{% endequation %} ועל ידי כך שנחלק ב-{% equation %}p{% endequation %} את שני האגפים נקבל {% equation %}m<p{% endequation %}, כפי שרצינו.

בשעה טובה הגענו אל החלק האחרון של ההוכחה: להוכיח שאם {% equation %}mp{% endequation %} הוא סכום של ארבעה ריבועים ו-{% equation %}1<m{% endequation %} אז קיים {% equation %}1\le n<m{% endequation %} כך שגם {% equation %}np{% endequation %} הוא סכום של ארבעה ריבועים. אז ראשית כל נכתוב:

{% equation %}mp=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{4}{% endequation %}

במילים אחרות, {% equation %}m{% endequation %} מחלק את הסכום הזה, כלומר {% equation %}x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{4}\equiv_{m}0{% endequation %}. כמו קודם, נרצה לבחור איברים ששקולים ל-{% equation %}x{% endequation %}-ים בצורה כזו שהם יהיו קטנים יחסית, אבל הפעם ביחס לגודל של {% equation %}m{% endequation %} ולא של {% equation %}p{% endequation %}. אז לכל {% equation %}1\le i\le4{% endequation %} נמצא {% equation %}y_{i}{% endequation %} כך ש-{% equation %}x_{i}\equiv_{m}y_{i}{% endequation %} ומתקיים ש-{% equation %}-\frac{m}{2}&lt;y_{i}\le\frac{m}{2}{% endequation %} (בכוונה לא כתבתי {% equation %}\left|y_{i}\right|\le\frac{m}{2}{% endequation %} כי עוד מעט אסתמך על כך שאפשר לבחור את ה-{% equation %}y_{i}{% endequation %}-ים כך שיהיו שונים מ-{% equation %}-\frac{m}{2}{% endequation %}). נקבל שיש {% equation %}n{% endequation %} כך ש-{% equation %}nm=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}+y_{4}^{4}\le\frac{m^{2}}{4}+\frac{m^{2}}{4}+\frac{m^{2}}{4}+\frac{m^{2}}{4}=m^{2}{% endequation %}, כלומר {% equation %}0\le n\le m{% endequation %}. מצאנו את ה-{% equation %}n{% endequation %} שלנו. מה שנשאר לעשות: להוכיח ש-{% equation %}n>0{% endequation %}, להוכיח ש-{% equation %}n<m{% endequation %}, ולהוכיח ש-{% equation %}np{% endequation %} הוא סכום של ארבעה ריבועים.

נניח ש-{% equation %}n=0{% endequation %}. זה אומר שבהכרח כל ה-{% equation %}y_{i}{% endequation %}-ים הם 0, ומכיוון ש-{% equation %}x_{i}\equiv_{m}y_{i}{% endequation %} נובע מכך ש-{% equation %}m{% endequation %} מחלק את כל ה-{% equation %}x_{i}{% endequation %}-ים. לכן {% equation %}m^{2}{% endequation %} מחלק את {% equation %}x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{4}=mp{% endequation %}. אם {% equation %}m^{2}|mp{% endequation %} נובע מכך ש-{% equation %}m|p{% endequation %}, וזו סתירה לכך ש-{% equation %}p{% endequation %} ראשוני (הנה, השתמשנו בזה שוב!). אז {% equation %}n\ne0{% endequation %}.

נניח ש-{% equation %}n=m{% endequation %}. מתי זה יכול לקרות? רק אם {% equation %}y_{i}=\frac{m}{2}{% endequation %} לכל {% equation %}1\le i\le4{% endequation %}, כלומר {% equation %}x_{i}\equiv_{m}\frac{m}{2}{% endequation %} לכל {% equation %}1\le i\le4{% endequation %}, ועל ידי העלאה בריבוע של האגפים ושל המודולוס נקבל {% equation %}x_{i}^{2}\equiv_{m^{2}}\frac{m^{2}}{4}{% endequation %}, כלומר {% equation %}mp\equiv_{m^{2}}m^{2}{% endequation %}, כלומר {% equation %}m^{2}|m\left(p-m\right){% endequation %} ולכן שוב נקבל {% equation %}m|p{% endequation %} - סתירה. אז {% equation %}n\ne m{% endequation %}.

כדי להראות ש-{% equation %}np{% endequation %} הוא סכום של ארבעה ריבועים, נסתכל קודם כל על שני הסכומים שכבר ראינו:

{% equation %}mp=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{4}{% endequation %}

{% equation %}nm=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}+y_{4}^{4}{% endequation %}

אנחנו כבר יודעים שמכפלה של שני סכומי ארבעה ריבועים היא בעצמה סכום של ארבעה ריבועים, אז על ידי כפל שתי המשוואות אני אקבל ש-{% equation %}npm^{2}{% endequation %} הוא סכום של ארבעה ריבועים. הבעיה היא ה-{% equation %}m^{2}{% endequation %} שתקוע בקצה המכפלה. כדי להיפטר ממנו, אני צריך להראות ש-{% equation %}npm^{2}=z_{1}^{2}+z_{2}^{2}+z_{3}^{2}+z_{4}^{2}{% endequation %} כך שלכל {% equation %}1\le i\le4{% endequation %} מתקיים {% equation %}m|z_{i}{% endequation %} - זה יסיים את זה סופית. כדי לראות את זה, אני חושש שאין מנוס מלשלוף שוב את הנוסחה שמציגה את מכפלת שני סכומי הריבועים כסכום ריבועים בעצמה:

{% equation %}\left(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}\right)\left(y_{1}^{2}+y_{2}^{2}+y_{3}^{2}+y_{4}^{2}\right)={% endequation %}

{% equation %}\left(x_{1}y_{1}-x_{2}y_{2}-x_{3}y_{3}-x_{4}y_{4}\right){}^{2}+\left(x_{1}y_{2}+x_{2}y_{1}+x_{3}y_{4}-x_{4}y_{3}\right)^{2}+{% endequation %}

{% equation %}\left(x_{1}y_{3}-x_{2}y_{4}+x_{3}y_{1}+x_{4}y_{2}\right)^{2}+\left(x_{1}y_{4}+x_{2}y_{3}-x_{3}y_{2}+x_{4}y_{1}\right)^{2}{% endequation %}

בנוסחה הזו אני הולך לעשות מניפולציה קטנה: אני יכול להחליף את {% equation %}y_{2},y_{3},y_{4}{% endequation %} במינוס שלהם - זה לא משפיע בכלל על אגף שמאל (כי אנחנו מעלים את המספרים הללו בריבוע) ובאגף ימין זה רק יגרום לביטויים שבתוך הסוגריים להיות יותר נוחים עבורי. עכשיו, אני צריך להוכיח שכל אחד מהביטויים הללו מתחלק ב-{% equation %}m{% endequation %}, ולכן אני אסתכל עליו מודולו {% equation %}m{% endequation %} ואשתמש בכך ש-{% equation %}x_{i}\equiv_{m}y_{i}{% endequation %}.

נקבל שהביטוי בסוגריים הראשונים, אחרי החלפת ה-{% equation %}y{% endequation %}-ים במינוסים שלהם ואחרי החלפת ה-{% equation %}y{% endequation %}-ים ב-{% equation %}x{% endequation %}-ים, הוא {% equation %}x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}{% endequation %}, והביטוי הזה שווה ממש ל-{% equation %}mp{% endequation %} ולכן בוודאי ששקול ל-0 מודולו {% equation %}m{% endequation %}.

נותרו שלושת הסוגריים האחרים ובכולם המבנה דומה. נסתכל על הסוגר הראשון מביניהם: הביטוי בו בהתחלה היה {% equation %}x_{1}y_{2}+x_{2}y_{1}+x_{3}y_{4}-x_{4}y_{3}{% endequation %}. אחרי החלפת {% equation %}y_{2},y_{3},y_{4}{% endequation %} במינוסים שלהם קיבלנו את {% equation %}x_{2}y_{1}-x_{1}y_{2}+x_{4}y_{3}-x_{3}y_{4}{% endequation %}. שימו לב לסימטריה! עכשיו, אחרי החלפת ה-{% equation %}y{% endequation %}-ים ב-{% equation %}x{% endequation %}-ים נקבל {% equation %}x_{2}x_{1}-x_{1}x_{2}+x_{4}x_{3}-x_{3}x_{4}=0{% endequation %}, כלומר קיבלנו שהביטוי שקול ל-0 מודולו {% equation %}m{% endequation %} ולכן מתחלק ב-{% equation %}m{% endequation %}. אותו דבר מטפל בכל יתר הביטויים שבסוגריים, אז ניצחנו!

המסקנה הסופית שלנו היא שכל מספר ניתן לייצוג כסכום של ארבעה ריבועים, אבל יש עוד שתי הערות צדדיות שאני רוצה לדבר עליהן כאן. ראשית, יש תוצאה חזקה אפילו יותר עבור ראשוניים ששקולים ל-1 מודולו {% equation %}4{% endequation %}: כל ראשוני כזה ניתן להצגה כסכום של <strong>שני</strong> ריבועים. זו אבחנה שהייתה קיימת כבר אצל פרמה ואוילר הוכיח; את ההוכחה <a href="http://www.gadial.net/2009/06/26/sums_of_squares_and_quadratic_reciprocity/">כבר הצגתי בבלוג</a> בעבר. אוילר הוא גם זה שמצא את הנוסחה שמציגה מכפלה של סכום של ארבעה ריבועים בתור סכום של ארבעה ריבועים בעצמו, אבל לא עלה בידיו למצוא את יתר ההוכחה - את זה עשה, כאמור, לגראנז', ב-1770. לא מעט שנים לאחר מכן, ב-1834, יעקובי הצליח להוכיח תוצאה חזקה בהרבה - נוסחה שנותנת, לכל מספר טבעי, את <strong>מספר</strong> הדרכים השונות לכתוב אותו כסכום של ארבעה ריבועים; במילים אחרות, נוסחה שמתארת את מספר הפתרונות השונים למשוואה הדיופנטית {% equation %}x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=n{% endequation %}. בפרט המספר הזה גדול תמיד מ-0 ולכן משפט לגראנז' נובע. רק מה, ההוכחות לטענה הזו מסובכות יותר; הפשוטה ביותר שאני מכיר היא של דיריכלה ומסתמכת על קרקטרי דיריכלה, שגם אותם <a href="http://www.gadial.net/2009/05/25/dirichlet_theorem_on_arithmetic_progressions/">כבר הצגתי בבלוג בעבר</a>. יהיה נחמד מאוד להציג את ההוכחה הזו מתישהו בבלוג, אבל לעת עתה אסתפק בלתת את הנוסחה: אם {% equation %}n{% endequation %} הוא מספר טבעי חיובי <strong>אי זוגי</strong> אז מספר הפתרונות בשלמים (כולל שליליים! ועם חשיבות לסדר!) למשוואה {% equation %}x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=n{% endequation %} הוא {% equation %}8\cdot\sum_{d|n}d{% endequation %} (שמונה כפול סכום המחלקים הטבעיים של {% equation %}n{% endequation %}), ואם {% equation %}n{% endequation %} הוא <strong>זוגי</strong> אז מספר הפתרונות הוא {% equation %}24\cdot\sum_{d|n}d{% endequation %} כאשר כאן ה-{% equation %}d{% endequation %}-ים הם רק המחלקים האי-זוגיים.

הנוסחה מגניבה לגמרי, אבל כשאני רואה אותה הדבר הראשון שאני תוהה לגביו הוא למה, לכל הרוחות, היא בכלל עובדת. לכן הוכחות הן דבר מעניין. לצערי, נצטרך לוותר עליה לבינתיים כי שולי הפוסט הזה צרים מלהכילה (מתי, מתי יימאס לי מהבדיחה הזו בסוף פוסטים של תורת המספרים?)

