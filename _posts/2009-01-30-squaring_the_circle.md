---
id: 181
title: "אז למה אי אפשר לרבע את העיגול?"
date: 2009-01-30 15:03:32
layout: post
categories: 
  - אלגברה מופשטת
social_media_share: true
---
כזכור, <a href="http://www.gadial.net/2009/01/06/field_extensions/">בפוסטים</a> <a href="http://www.gadial.net/2009/01/28/field_extensions_extended/">האחרונים</a> אנו עוסקים ב<a href="http://www.gadial.net/2008/12/23/straightedge_and_compas_constructions/">בניות בסרגל ומחוגה.</a> על בניות כאלו אפשר לחשוב כ"משחק" שבו יוצרים מספרים חדשים ממספרים קיימים בעזרת ארבע פעולות החשבון והוצאת שורש, כשהמספר שממנו מתחילים הוא 1. האתגר: להראות שכמה מספרים, שמתאימים לבעיות בנייה "קלאסיות" שהטרידו את היוונים, אינם ניתנים לבנייה במשחק הזה.

בפוסט הקודם, בעזרת כמה תוצאות בסיסיות מהתורה של הרחבת שדות, הראיתי שאפשר להתאים לכל מספר ממשי ערך כלשהו - ה"מימד" שלו מעל הרציונליים. לא חשוב כרגע מה המשמעות של המימד הזה (דיברתי על כך בפוסט הקודם), אלא רק המסקנה הסופית - אם מספר ממשי הוא ניתן לבנייה באמצעות סרגל ומחוגה, המימד שלו הוא חזקה של 2.

כעת אפשר להרוס תכף ומייד את אחת מהבעיות הגאומטריות של היוונים - הכפלת נפח הקוביה. הבעיה, כזכור, אומרת כך: יש לנו קוביה שאורך צלעה 1. האם ניתן לבנות קוביה שנפחה כפול? נפח קוביה עם צלע 1 הוא 1, ומכאן שנפח כפול הוא 2; אם {% equation %}a{% endequation %} הוא צלע קוביה אז נפחה הוא {% equation %}a^3{% endequation %}, ומכאן שכדי לבנות קוביה עם נפח 2 צריך לבנות צלע עם אורך {% equation %}\sqrt[3]{2}{% endequation %}. אלא שקל להראות שהמימד של המספר הזה מעל הרציונליים הוא 3, שאינו חזקה של 2, ולכן לא ניתן לבנות אותו. סוף הסיפור.

הסבר נוסף עבור מי שרוצה לדעת איך הולך ה"קל להראות" וקרא את הפוסט הקודם: השורש השלישי של 2 מאפס את הפולינום {% equation %}x^3-2{% endequation %}. הפולינום הזה הוא אי פריק מעל הרציונליים, כי הוא פולינום ממעלה 3 שאין לו שורש רציונלי (כל פולינום ממעלה קטנה מ-4 שאין לו שורש רציונלי אינו פריק מעל הרציונליים). לכן זהו הפולינום המינימלי שמאפס את {% equation %}\sqrt[3]{2}{% endequation %} (אחרת היינו מחלקים את  {% equation %}x^3-2{% endequation %} בפולינום המינימלי, ומקבלים פולינום קטן עוד יותר שמאפס את {% equation %}\sqrt[3]{2}{% endequation %} - השארית של החלוקה - וזו הייתה סתירה למינימליות). כזכור, בפוסט הקודם הראיתי שהדרגה של הפולינום המינימלי היא המימד של האיבר.

הבעיה הבאה שאני רוצה לטפל בה היא בעיית חלוקת זווית לשלושה חלקים שווים. במילים אחרות, אם כבר בנינו שני קטעים כך שאחד מהקצוות של כל אחד מהם הוא בראשית הצירים, אפשר לחשוב על כך כאילו בנינו את הזווית שביניהם (יש שתי זוויות ביניהם, אז בעצם בנינו שתי זוויות שמשלימות זו את זו ל-360 מעלות). אם כבר בנינו את הזווית {% equation %}\alpha{% endequation %} האם אפשר גם לבנות את הזווית {% equation %}\frac{\alpha}{3}{% endequation %}?

יש מקרים שבהם זה אפשרי - אפשר לבנות זווית של 60 מעלות, ולכן אפשר לחלק לשלוש את הזווית 180. עם זאת, כדי לראות שאי אפשר לעשות את זה באופן כללי מספיק להראות דוגמה נגדית אחת - וזווית של 60 מעלות היא דוגמה נגדית שכזו. אי אפשר לחלק אותה לשלושה חלקים, כלומר אי אפשר לבנות זווית של 20 מעלות.

כדי לראות זאת צריך לתרגם את בניית הזווית לבנייה של מספר ממשי כלשהו. אם יש לנו שני קווים מאותו אורך, עם זווית של {% equation %}\alpha{% endequation %} מעלות ביניהם, ואנו מורידים אנך מאחד לשני, אורך האנך יהיה {% equation %}\cos(\alpha){% endequation %}, שהוא מספר ממשי. אם כן, מספיק להראות שלא ניתן לבנות את הקוסינוס של 20 מעלות. באמצעות שימוש בכך שקוסינוס של 60 מעלות הוא חצי וכל מני תעלולים טריגונומטריים שסתם מעייף לפרט אפשר להגיע לכך שאם ניתן לבנות את קוסינוס 20 אז אפשר לבנות מספר  {% equation %}\theta{% endequation %} שהמימד שלו מעל הממשיים הוא 3, וסיימנו (אפשר להראות שהוא מקיים {% equation %}\theta^3-3\theta-1=0{% endequation %}, כלומר מאפס את הפולינום {% equation %}x^3-3x-1{% endequation %}, ולא קשה להראות שלפולינום הזה אין שורש מעל הרציונליים ולכן הוא אי פריק, שכן שורש מעל הרציונליים של פולינום מתוקן חייב לחלק את המקדם החופשי, שהוא 1 במקרה הזה).

המקרה הפשוט ביותר, שהוא גם המסובך ביותר, הוא של ריבוע העיגול. ריבוע העיגול דורש בניית ריבוע ששטחו שווה לשטח עיגול נתון, ואפשר להראות שמספיק לדעת איך בונים ריבוע כזה עבור עיגול היחידה - העיגול שרדיוסו 1 ולכן שטחו הוא בדיוק פאי. מכיוון ששטח ריבוע הוא ריבוע אורך הצלע שלו (מכאן מגיעה המילה "ריבוע" בהקשר של חזקה שנייה, כמובן) זה שקול לבנייה של שורש פאי.

כאן אנחנו מתקשרים סוף סוף למאמר שבעקבותיו <a href="http://www.gadial.net/2008/12/08/bad_math_pi_undefinable/">התחלתי לכתוב</a> את כל העסק הזה - בשנת 1882 הוכיח לינדמן (בהתבסס על תוצאה דומה קודמת של הרמיט עבור המספר e) כי פאי הוא טרנסנדנטי מעל הרציונליים, כלומר אינו מאפס אף פולינום במקדמים רציונליים. על פי מה שהסברתי בפוסט הקודם, זה אומר שהמימד שלו הוא אינסופי. קל מאוד להראות שאם שורש פאי כן היה מאפס פולינום כלשהו במקדמים רציונליים, אז היינו מקבלים מכך שקיים פולינום אחר במקדמים רציונליים (איזה?) שמאפס את פאי - כלומר, גם שורש פאי הוא טרנסנדנטי, כלומר ממימד אינסופי ובפרט לא ממימד שהוא חזקה של 2, וגמרנו.

מה המלכוד? שההוכחה שפאי הוא טרנסנדנטי אינה פשוטה כלל וכלל. אמנם, הטרנסנדנטיות היא overkill מסויים - כל מה שצריך לעשות הוא להראות הוא שאם קיים פולינום מינימלי שמאפס את פאי (לא קיים, זה בדיוק העניין, אבל אפשר לשחק ב"מה אילו") אז דרגתו איננה חזקה של 2. אולי יש דרך פשוטה יחסית להוכיח זאת - איני מכיר אותה. כדאי לציין שעד להוכחתו של לינדמן, הבעיה של ריבוע העיגול נחשבה פתוחה (שתי האחרות חוסלו כבר שנים רבות קודם לכן), כך שאולי זו בכל זאת הדרך המיידית ביותר להוכיח זאת.

זהו, כך נסתם הגולל על בעיות שהיו פתוחות 2,000 שנים. ההוכחה שהצגתי אמנם אינה מלאה ויש עוד מה לפרט ולדקדק, אך אלו הם כל הרעיונות שיש בה. כל סטודנט למתמטיקה מסוגל, כבר בשלב לא מתקדם של התואר שלו, להבין את כל פרטי הבניות עד תומן (למעט אולי ההוכחה שפאי טרנסנדנטי). כמובן שיש כאלו שעבורם זה לא מספיק - גם היום צצים לא מעט אנשים שטוענים שהם יודעים לחלק זווית לשלוש או לרבע את העיגול. לרוב זה נובע מכך שהם לא יודעים מתמטיקה, או לא מבינים עד הסוף מהם "כללי המשחק" הפורמליים של בניה בסרגל ומחוגה (כך למשל קל מאוד לחלק זווית לשלושה חלקים אם מאפשרים סימון של אורכים על הסרגל). <a href="http://www.gadial.net/2007/10/13/pi_law/">כבר דיברתי כאן</a> על הטרחן הידוע ביותר (אמנם, מלפני למעלה מ-100 שנה, אך לאחר הוכחתו של לינדמן) שסבר שהוא מסוגל לרבע את המעגל - אותו ברנש שמאחורי "חוק הפאי של אינדיאנה".

אנא, הפיצו את הבשורה לחבריכם - הבעיות הללו מתו ונקברו. אל תשחתו את זמנכם על פתרונן. אם נתקלתם במישהו שטוען שהוא יודע לרבע את העיגול, ברחו מהר ככל הניתן!
