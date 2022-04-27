---
title: "מה בעצם הולך בטריגונומטריה בתיכון? (חלק ה' - משפט הקוסינוסים)"
layout: post
categories:
  - כללי
tags:
  - טריגונומטריה
image: "2021/cosine_formula3.png"
description: 'משפט הקוסינוסים הוא לא "משפט הסינוסים 2 - הנקמה" אלא יותר "משפט פיתגורס 2 - הפעם עם משולש לא ישר זווית". ההוכחה דווקא די קצרה והמשפט די מועיל'
---

אנחנו מתקדמים יפה מאוד בסדרת הפוסטים שלי שמטרתה להבין את הנוסחאות הטריגונומטריות:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas.png" alt=""/>

בפעם הקודמת ראינו את משפט הסינוסים וכעת נדבר על <strong>משפט הקוסינוסים</strong>. למשפט הזה אין קשר ישיר למשפט הסינוסים והוא לא "גרסה של משפט הסינוסים רק עם קוסינוסים" אלא זה משהו שונה למדי - סוג של הכללה של <strong>משפט פיתגורס</strong>. אז בואו ניזכר מהו משפט פיתגורס. לשם כך נזדקק למשולש ישר זווית - איך לא. כל מה שאנחנו עוסקים הוא כל היום להתעסק במשולשים ישרי זווית.

<img src="{{site.baseurl}}{{site.post_images}}/2021/cosine_formula1.png" alt=""/>

אם כן, בואו נסתכל על משולש ישר זווית שהיתר שלו היא מאורך {% equation %}c{% endequation %} והצלעות האחרות הן מאורך {% equation %}a,b{% endequation %}. <strong>משפט פיתגורס</strong> אומר ש-{% equation %}a^{2}+b^{2}=c^{2}{% endequation %}. יש שלל שיטות להוכיח אותו אבל נעזוב את זה רגע. בואו נסתכל עכשיו על משולש כללי, כזה שאינו ישר זווית:

<img src="{{site.baseurl}}{{site.post_images}}/2021/cosine_formula2.png" alt=""/>

בואו נקרא לזווית {% equation %}\angle ACB{% endequation %} שמול {% equation %}AB{% endequation %} בשם {% equation %}\gamma{% endequation %}. אז משפט הקוסינוסים אומר את הדבר הבא:

<ul> <li>{% equation %}a^{2}+b^{2}-2ab\cos\gamma=c^{2}{% endequation %}</li>

</ul>

אם המשולש הוא ישר זווית, כלומר {% equation %}\gamma=90^{\circ}{% endequation %}, אז {% equation %}\cos\gamma=0{% endequation %} ולכן הביטוי {% equation %}-2ab\cos\gamma{% endequation %} מתאפס ואנחנו חוזרים למקרה הרגיל של משפט פיתגורס. אבל אם המשולש אינו ישר זווית, אנחנו רואים שמשפט פיתגורס מתקיים עם "תיקון" שמתחשב בזווית בין הצלעות {% equation %}AC{% endequation %} ו-{% equation %}BC{% endequation %}. ייתכן שהביטוי {% equation %}ab\cos\gamma{% endequation %} נראה מוכר; זה מה שנקרא <strong>המכפלה הסקלרית</strong> של שתי הצלעות, אבל אני לא אכנס לזה בפוסט.

השימושיות של המשפט ברורה - אם משולש נתון לנו באמצעות אורכי שתי צלעות והזווית ביניהם, אנחנו יכולים להסיק ממנו את אורך הצלע השלישית; זה דומה למה שקרה במשפט הסינוסים, שם היכרות עם צלע אחד ושתי זוויות נתנה לנו את היתר.

איך מוכיחים את המשפט? ובכן, אם אתן עוקבות אחרי סדרת הפוסטים הזו מתחילתה, אתן כבר יודעות מה הולך לבוא כרגע! כן! הנה הוא בא! ה<strong>אנך</strong> מגיע! אוי לאאאא!

<img src="{{site.baseurl}}{{site.post_images}}/2021/cosine_formula3.png" alt=""/>

כן, זה המצב. אני יודע לעשות רק טריק אחד ואיכשהו הוא פותר לי את הכל שוב ושוב. וזה דבר טוב! זה מראה שיחסית קל להגיע אל כל הנוסחאות הללו. עדיין, איך האנך עוזר לנו כאן? ובכן, אם נסמן את הזווית {% equation %}\angle CAB{% endequation %} ב-{% equation %}\alpha{% endequation %} ואת {% equation %}\angle ABC{% endequation %} ב-{% equation %}\beta{% endequation %}, כרגיל, נקבל את האורכים של {% equation %}AD{% endequation %} ושל {% equation %}BD{% endequation %} באופן הבא:

{% equation %}\left|AD\right|=b\cos\alpha{% endequation %}

{% equation %}\left|BD\right|=a\cos\beta{% endequation %}

וזה נחמד מאוד כי {% equation %}\left|AB\right|=c{% endequation %} הוא סכום של שני אלו:

{% equation %}c=\left|AB\right|=\left|AD\right|+\left|BD\right|=a\cos\beta+b\cos\alpha{% endequation %}

עכשיו, אנחנו רוצים להגיע אל {% equation %}c{% endequation %} בריבוע; דרך אחת לעשות זאת היא להכפיל את שני אגפי המשוואה ב-{% equation %}c{% endequation %} ולקבל

<ul> <li>{% equation %}c^{2}=ac\cos\beta+bc\cos\alpha{% endequation %}</li>

</ul>

אני רוצה גם את {% equation %}a^{2},b^{2}{% endequation %} אז אני יכול להתבסס על כך שאפשר לעשות את אותו חישוב בדיוק גם עבורם, ולקבל

<ul> <li>{% equation %}a^{2}=ab\cos\gamma+ac\cos\beta{% endequation %}</li>


<li>{% equation %}b^{2}=ab\cos\gamma+bc\cos\alpha{% endequation %}</li>

</ul>

עכשיו, בואו נחבר את שתי המשוואות הללו:

{% equation %}a^{2}+b^{2}=2ab\cos\gamma+\left(ac\cos\beta+bc\cos\alpha\right){% endequation %}

בבירור הגורם בסוגריים הוא פשוט {% equation %}c^{2}{% endequation %} ולכן אחרי שנעביר אגף נקבל

<ul> <li>{% equation %}a^{2}+b^{2}-2ab\cos\gamma=c^{2}{% endequation %}</li>

</ul>

וזה מה שרצינו להוכיח. ממש פשוט! אולי אפילו פשוט מדי! שוב פעם הנחתי באופן מובלע שהאנך שאני מוריד יהיה <strong>בתוך</strong> המשולש. צריך גם לטפל במקרה שבו זה לא קורה.

<img src="{{site.baseurl}}{{site.post_images}}/2021/cosine_formula4.png" alt=""/>

ובכן, ראינו את המקרה הזה גם בפוסט הקודם על משפט הסינוסים, והטריק שם היה שאפשר לקבל את {% equation %}\left|AB\right|{% endequation %} הפעם באמצעות <strong>הפרש</strong>: {% equation %}\left|AB\right|=\left|BD\right|-\left|AD\right|{% endequation %}. האם אנו יודעים לחשב את שני האיברים שבאגף ימין? ובכן, {% equation %}\left|BD\right|=a\cos\beta{% endequation %} (על פי המשולש {% equation %}BCD{% endequation %}) ו-{% equation %}\left|AD\right|=b\cos\left(180^{\circ}-\alpha\right){% endequation %} (על פי המשולש {% equation %}ACD{% endequation %}). עכשיו, בפוסט הקודם הסתמכנו על כך ש-{% equation %}\sin\left(180^{\circ}-\alpha\right)=\sin\alpha{% endequation %} אבל בקוסינוסים זה לא הולך ככה אלא עם סימן מינוס:

{% equation %}\cos\left(180^{\circ}-\alpha\right)=-\cos\alpha{% endequation %}

ולכן נקבל

{% equation %}\left|AD\right|=b\cos\left(180^{\circ}-\alpha\right)=-b\cos\alpha{% endequation %}

למרבה השמחה, זה מסתדר לנו בול עם החיסור ב-{% equation %}\left|AB\right|=\left|BD\right|-\left|AD\right|{% endequation %} ואנחנו מקבלים

{% equation %}\left|AB\right|=a\cos\beta+b\cos\alpha{% endequation %}

בדיוק כמו שקרה במקרה הקודם, ומכאן ההוכחה ממשיכה כרגיל.

רגע, זה הכל? ובכן, כן, זה כמעט וסיים לנו את כל דף הנוסחאות ואני חייב להודות שזה היה ממש קל, יחסית. מה נשאר לנו? להבין את החלק בדף הנוסחאות שמדבר על <strong>רדיאנים</strong>. אז נכון שיש לי פוסט בנושא אבל הוא נכתב לפני שנים רבות ולא יזיק לכתוב עוד אחד אם אנחנו כבר כאן; זה יהיה בפעם הבאה. 