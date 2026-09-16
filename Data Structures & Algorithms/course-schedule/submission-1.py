class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create a dictionary where:
        # key   = course
        # value = list of prerequisites needed for that course
        #
        # Example: numCourses = 4
        # {0: [], 1: [], 2: [], 3: []}
        preMap = {i: [] for i in range(numCourses)}

        # Each pair is [course, prerequisite]
        #
        # Example:
        # prerequisites = [[1,0], [2,1]]
        #
        # Course 1 requires 0
        # Course 2 requires 1
        #
        # preMap becomes:
        # {
        #   0: [],
        #   1: [0],
        #   2: [1]
        # }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        # Contains courses in our CURRENT DFS path.
        #
        # Important: this is NOT every course we've ever visited.
        # It only tracks the path we are currently exploring.
        visiting = set()


        def dfs(crs):

            if crs in visiting:
                # YES — if the course is already in the current path,
                # we have come back to a course we were already trying
                # to complete.
                #
                # That means there is a CYCLE.
                #
                # Example:
                # 0 requires 1
                # 1 requires 2
                # 2 requires 0
                #
                # 0 -> 1 -> 2 -> 0
                #
                # We cannot finish these courses.
                return False


            if preMap[crs] == []:
                # This course has NO prerequisites,
                # OR we already proved its prerequisites are finishable.
                #
                # Either way, this course can be completed.
                return True


            # We are now exploring this course.
            # Add it to the CURRENT DFS path.
            visiting.add(crs)


            # Look at every prerequisite needed for this course.
            for pre in preMap[crs]:

                # Before we can finish crs,
                # we must be able to finish its prerequisite.
                if not dfs(pre):
                    # If the prerequisite eventually leads to a cycle,
                    # then crs cannot be completed either.
                    return False


            # We successfully checked all prerequisites.
            # Remove crs because we're DONE exploring this path.
            visiting.remove(crs)


            # Mark this course as completed/verified.
            #
            # We're basically saying:
            # "We already checked this course and know it's safe."
            #
            # This prevents us from doing the same DFS again later.
            preMap[crs] = []

            return True


        # We need to check EVERY course because the graph
        # might have separate/disconnected sections.
        for c in range(numCourses):

            if not dfs(c):
                # If ANY course leads to a cycle,
                # we cannot finish all courses.
                return False

        # We checked every course and found no cycles.
        return True